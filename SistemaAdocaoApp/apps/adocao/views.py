from django.shortcuts import render
from rest_framework import viewsets
from .models import Adocao
from .serializer import AdocaoSerializer

# Create your views here.

class AdocaoViewSet(viewsets.ModelViewSet):
    queryset = Adocao.objects.all()
    serializer_class = AdocaoSerializer