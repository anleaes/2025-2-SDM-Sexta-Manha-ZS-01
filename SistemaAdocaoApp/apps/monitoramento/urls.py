from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'monitoramentos'

router = routers.DefaultRouter()
router.register('', views.MonitoramentoPosAdocaoViewSet, basename='monitoramentos')

urlpatterns = [
    path('', include(router.urls) )
]