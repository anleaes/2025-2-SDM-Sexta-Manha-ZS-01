from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'agendamentos'

router = routers.DefaultRouter()
router.register('', views.AgendamentoVisitaViewSet, basename='agendamentos')

urlpatterns = [
    path('', include(router.urls) )
]