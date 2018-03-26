from rest_framework import serializers
from animal_app.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'name', 'number')


'''
class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    number = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        """
        Create and return new Zoo pet
        """
        return Animal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Zoo pets, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance
'''
