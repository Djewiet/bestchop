from django.shortcuts import render

# Create your views here.
from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework import viewsets
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ListCreateUserProfile(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UpdateDeleteUserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
