from django.shortcuts import render
from rest_framework import viewsets
from .models import Campanha
from .serializer import CampanhaSerializer

# Create your views here.
class CampanhaViewSet(viewsets.ModelViewSet):
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer