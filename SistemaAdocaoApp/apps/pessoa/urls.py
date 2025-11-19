from django.urls import path,include
from rest_framework import routers
from . import views

app_name = 'pessoa'


router = routers.DefaultRouter()
router.register('', views.pessoaViewSet, basename='pessoa')
urlpatterns = [
    path('', include(router.urls) )
]