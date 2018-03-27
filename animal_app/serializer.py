from rest_framework import serializers
from animal_app.models import Animal
from django.contrib.auth.models import User


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Animal
        fields = ('url', 'pk', 'name', 'number', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    animal = serializers.HyperlinkedRelatedField(many=True,view_name='animal-detail',
                                                 read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'animal')
