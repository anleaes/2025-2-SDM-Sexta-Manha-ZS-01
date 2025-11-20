from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'agendamento'

router = routers.DefaultRouter()
router.register('', views.AgendamentoVisitaViewSet, basename='agendamento')

urlpatterns = [
    path('', include(router.urls) )
]