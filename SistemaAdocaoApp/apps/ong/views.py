from django.shortcuts import render
from rest_framework import viewsets
from .models import ong
from .serializer import ongSerializer

# Create your views here.
class ongViewSet(viewsets.ModelViewSet):
    queryset = ong.objects.all()
    serializer_class = ongSerializer