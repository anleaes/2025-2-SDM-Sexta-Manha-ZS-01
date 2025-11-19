
from .models import pessoa
from rest_framework import serializers

class pessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = pessoa
        fields = '__all__'
        
