from .models import ONG
from rest_framework import serializer

class ONGSerializer(serializer.ModelSerializer):
    class Meta:
        
        model = ONG
        fields = '__all__'