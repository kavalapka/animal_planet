from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from animal_app import views


urlpatterns = [
    url(r'^animal/$', views.AnimalList.as_view(), name='index'),
    url(r'^animal/(?P<pk>[0-9]+)/$', views.AnimalDetail.as_view(), name='detail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
