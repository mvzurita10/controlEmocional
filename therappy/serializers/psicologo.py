from rest_framework import serializers
from therappy.models.psicologo import Psicologo

class PsicologoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psicologo
        fields = '__all__'
