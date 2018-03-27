from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from animal_app import views


router = DefaultRouter()
router.register(r'animal', views.AnimalViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls),)
]
