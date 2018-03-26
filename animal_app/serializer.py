from rest_framework import serializers
from animal_app.models import Animal
from django.contrib.auth.models import User


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('pk', 'name', 'number', 'owner')


class UserSerializer(serializers.ModelSerializer):
    animal = serializers.PrimaryKeyRelatedField(many=True, queryset=Animal.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'animal')
