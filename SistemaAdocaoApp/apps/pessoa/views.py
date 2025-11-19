from django.shortcuts import render
from rest_framework import viewsets
from .models import pessoa
from .serializer import pessoaSerializer

# Create your views here.
class pessoaViewSet(viewsets.ModelViewSet):
    queryset = pessoa.objects.all()
    serializer_class = pessoaSerializer 
    