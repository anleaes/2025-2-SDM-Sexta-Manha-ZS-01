
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pessoa'

router = routers.DefaultRouter()
router.register('', views.pessoaViewSet, basename='pessoa')

urlpatterns = [
    path('', include(router.urls) )
]