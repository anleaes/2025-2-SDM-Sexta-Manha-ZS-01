from django.shortcuts import render
from rest_framework import viewsets
from .models import ONG
from .serializer import ONGSerializer

# Create your views here.
class ONGViewSet(viewsets.ModelViewSet):
    queryset = ONG.objects.all()
    serializer_class = ONGSerializer
    