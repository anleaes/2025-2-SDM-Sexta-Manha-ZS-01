from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Adocao'
router = routers.DefaultRouter()
router.register('', views.AnimalViewSet, basename='Adocao')

urlpatterns = [
    path('', include(router.urls) )
]