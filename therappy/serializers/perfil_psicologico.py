from rest_framework import serializers
from therappy.models.perfil_psicologico import PerfilPsicologico

class PerfilPsicologicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilPsicologico
        fields = '__all__'
