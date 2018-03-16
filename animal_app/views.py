from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render


from animal_app.models import Animal


def index(request):
    latest_animal_list = Animal.objects.order_by('-id')[:5]
    template = loader.get_template('animals/index.html')

    context = {'latest_animal_list': latest_animal_list}
    return HttpResponse(template.render(context))

class based_view:
    pass

def detail(request, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
    except Animal.DoesNotExist:
        raise Http404("Animal does not exist")
    return render(request, 'animals/detail.html', {'animal': animal})
