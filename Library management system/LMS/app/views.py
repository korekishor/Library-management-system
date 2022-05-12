from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Books
from .serializers import BookSerializer
from rest_framework.decorators import permission_classes

@permission_classes(permissions.IsAdminUser,)
@api_view(['POST'])
def create(request):
    s=BookSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes(permissions.IsAuthenticated,)
@api_view(['GET'])
def read(request):
    books = Books.objects.all()
    seridata=BookSerializer(books,many=True)
    return Response (seridata.data)

@permission_classes(permissions.IsAdminUser,)
@api_view(['POST'])
def update(request,pk):
    b=Books.objects.get(id=pk)
    bs=BookSerializer(b,data=request.data)
    if bs.is_valid():
        bs.save()
        return Response('object updated')
    return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes(permissions.IsAdminUser,)
@api_view(['GET'])
def delete(request,pk):
    b=Books.objects.get(id=pk)
    b.delete()
    return Response('object deleted')
