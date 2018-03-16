from django.http import HttpResponse

from animal_app.models import Animal


def index(request):
    Animal
    return HttpResponse("Hello, world. You're at the Animals index.")

