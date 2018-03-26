from rest_framework import generics
from rest_framework import permissions
from django.views.generic.base import TemplateView
from animal_app.models import Animal
from animal_app.serializer import AnimalSerializer, UserSerializer
from django.contrib.auth.models import User


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
