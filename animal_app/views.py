from rest_framework import generics, permissions
from rest_framework import renderers
from django.views.generic.base import TemplateView
from animal_app.models import Animal
from animal_app.serializer import AnimalSerializer, UserSerializer
from django.contrib.auth.models import User
from animal_app.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'animal':reverse('animal-list', request=request, format=format)
    })


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
