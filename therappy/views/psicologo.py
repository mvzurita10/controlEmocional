from rest_framework import viewsets
from therappy.models.psicologo import Psicologo
from therappy.serializers.psicologo import PsicologoSerializer

class PsicologoViewSet(viewsets.ModelViewSet):
    queryset = Psicologo.objects.all().order_by('-id')
    serializer_class = PsicologoSerializer
    search_fields = ['especialidad', 'universidad']
    filterset_fields = ['disponible']
