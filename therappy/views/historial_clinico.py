from rest_framework import viewsets
from therappy.models.historial_clinico import HistorialClinico
from therappy.serializers.historial_clinico import HistorialClinicoSerializer

class HistorialClinicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialClinico.objects.all()
    serializer_class = HistorialClinicoSerializer
