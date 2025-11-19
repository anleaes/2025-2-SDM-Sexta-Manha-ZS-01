from django.shortcuts import render
from .models import pessoa
from .serializer import pessoaSerializer
from rest_framework import viewsets 

# Create your views here.
class pessoaViewSet(viewsets.ModelViewSet):
    queryset = pessoa.objects.all()
    serializer_class = pessoaSerializer 
