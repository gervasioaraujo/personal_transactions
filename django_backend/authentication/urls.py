from django.urls import include, path
from rest_framework import routers
from .views import UserRegisterView, UserLoginView


urlpatterns = [
    path('register', UserRegisterView.as_view()),
    path('login', UserLoginView.as_view()),
]
