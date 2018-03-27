from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from animal_app import views


urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root,),
    url(r'^animal/$', views.AnimalList.as_view(), name='animal-list'),
    url(r'^animal/(?P<pk>[0-9]+)/$', views.AnimalDetail.as_view(), name='animal-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
])


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
