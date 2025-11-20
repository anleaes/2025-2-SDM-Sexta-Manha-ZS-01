from .models import AgendamentoVisita
from rest_framework import serializers

class AgendamentoVisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendamentoVisita
        fields = '__all__'  