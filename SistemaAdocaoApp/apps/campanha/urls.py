from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'campanha'

router = routers.DefaultRouter()
router.register('', views.CampanhaViewSet, basename='campanha')

urlpatterns = [
    path('', include(router.urls) )
]