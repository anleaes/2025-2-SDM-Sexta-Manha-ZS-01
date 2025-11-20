from .models import Campanha
from rest_framework import serializers

class CampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Campanha
        fields = '__all__'