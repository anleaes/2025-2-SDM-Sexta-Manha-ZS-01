from rest_framework import serializer
from .models import pessoa

class pessoaSerializer(serializer.ModelSerializer):
    
    class Meta:
        model = pessoa
        fields = '__all__'
