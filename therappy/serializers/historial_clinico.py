from rest_framework import serializers
from therappy.models.historial_clinico import HistorialClinico

class HistorialClinicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialClinico
        fields = '__all__'
