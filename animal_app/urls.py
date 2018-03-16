from django.conf.urls import url
from django.urls import path

from animal_app.views import AnimalsView, AnimalDetail

urlpatterns = [
    path('', AnimalsView.as_view(), name='index'),
    url(r'^(?P<id>[0-9]+)/$', AnimalDetail.as_view(), name='detail'),
]
