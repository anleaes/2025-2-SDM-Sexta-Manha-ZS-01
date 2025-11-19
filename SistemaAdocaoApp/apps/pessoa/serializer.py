from rest_framework import serializers
from .models import pessoa

class pessoaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = pessoa
        fields = '__all__'
