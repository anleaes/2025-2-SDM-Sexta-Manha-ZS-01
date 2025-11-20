from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'adocao'
router = routers.DefaultRouter()
router.register('', views.AdocaoViewSet, basename='adocao')

urlpatterns = [
    path('', include(router.urls) )
]