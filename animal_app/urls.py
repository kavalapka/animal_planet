from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from animal_app import views


urlpatterns = [
    path('', views.AnimalList.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.AnimalDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
