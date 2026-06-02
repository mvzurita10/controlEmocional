from rest_framework import viewsets
from therappy.models.cita import Cita
from therappy.serializers.cita import CitaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all().order_by('-id')
    serializer_class = CitaSerializer
    search_fields = ['motivo', 'estado']
    filterset_fields = ['estado', 'fecha']
