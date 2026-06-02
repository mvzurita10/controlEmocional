from rest_framework import viewsets
from therappy.models.perfil_psicologico import PerfilPsicologico
from therappy.serializers.perfil_psicologico import PerfilPsicologicoSerializer

class PerfilPsicologicoViewSet(viewsets.ModelViewSet):
    queryset = PerfilPsicologico.objects.all()
    serializer_class = PerfilPsicologicoSerializer
