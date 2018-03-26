from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.views.generic.base import TemplateView
from animal_app.models import Animal
from animal_app.serializer import AnimalSerializer



class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()



'''class AnimalDetail(APIView):
    def get_object(self, id):
        try:
            return Animal.objects.get(id=id)
        except Animal.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        animal  = self.get_object(id)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        animal = self.get_object(id)
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        animal = self.get_object(id)
        animal.delete()
        return Response(status.HTTP_204_NO_CONTENT)
'''

'''class AnimalsView(TemplateView):

    template_name = "animals/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_animal_list'] = Animal.objects.order_by('-id')[:5]
        return context



class AnimalDetail(TemplateView):

    template_name = "animals/detail.html"

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            animal_id = kwargs['id']
            context['animal'] = Animal.objects.get(id=animal_id)
        except Animal.DoesNotExist:
            raise Http404("Animal does not exist")
        return context
'''
