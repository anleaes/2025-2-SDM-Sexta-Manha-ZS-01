from .models import ong
from rest_framework import serializers

class ongSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = ong
        fields = '__all__'