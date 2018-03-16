from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views.generic.base import TemplateView

from animal_app.models import Animal


class AnimalsView(TemplateView):

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
