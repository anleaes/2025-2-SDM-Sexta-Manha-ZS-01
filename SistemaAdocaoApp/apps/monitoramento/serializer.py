from .models import MonitoramentoPosAdocao
from rest_framework import serializers

class MonitoramentoPosAdocaoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MonitoramentoPosAdocao
        fields = '__all__'