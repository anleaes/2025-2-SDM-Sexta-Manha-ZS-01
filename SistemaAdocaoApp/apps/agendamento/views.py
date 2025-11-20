from django.shortcuts import render
from rest_framework import viewsets
from .models import AgendamentoVisita
from .serializer import AgendamentoVisitaSerializer

# Create your views here.

class AgendamentoVisitaViewSet(viewsets.ModelViewSet):
    queryset = AgendamentoVisita.objects.all()
    serializer_class = AgendamentoVisitaSerializer