from django.shortcuts import render
from rest_framework import viewsets
from .models import MonitoramentoPosAdocao
from .serializer import MonitoramentoPosAdocaoSerializer

# Create your views here.

class MonitoramentoPosAdocaoViewSet(viewsets.ModelViewSet):
    queryset = MonitoramentoPosAdocao.objects.all()
    serializer_class = MonitoramentoPosAdocaoSerializer