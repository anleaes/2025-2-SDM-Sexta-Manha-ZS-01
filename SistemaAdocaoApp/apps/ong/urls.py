from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ONG'

router = routers.DefaultRouter()
router.register('', views.ONGViewSet, basename='ONG')
urlpatterns = [
    path('', include(router.urls) )
]