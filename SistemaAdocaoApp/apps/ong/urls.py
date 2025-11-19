from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ong'

router = routers.DefaultRouter()
router.register('', views.ongViewSet, basename='ong')
urlpatterns = [
    path('', include(router.urls) )
]