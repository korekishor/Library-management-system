from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import generics,mixins
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class UserRegistrationView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserRegistrationSerializer
  permission_classes = (permissions.AllowAny,)


class UserLoginView(mixins.CreateModelMixin,generics.GenericAPIView):
  queryset = User.objects.all()
  serializer_class = UserLoginSerializer
  permission_classes = (permissions.AllowAny,)

  def post(self, request, *args, **kwargs):
    request.POST._mutable=True
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      headers = self.get_success_headers(serializer.data)
      d=serializer.data.copy()
      d.update(token)
      return Response(d, status=status.HTTP_201_CREATED,headers=headers)
    return Response(status=status.HTTP_400_BAD_REQUEST)
