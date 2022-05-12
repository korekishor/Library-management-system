from django.urls import path
from .views import UserLoginView, UserRegistrationView
urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    ]