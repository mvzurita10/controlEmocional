from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from therappy.permissions import IsAdminOrPsicologoOrReadOnly
from therappy.models.perfil_psicologico import PerfilPsicologico
from therappy.serializers.perfil_psicologico import PerfilPsicologicoSerializer

class PerfilPsicologicoViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilPsicologicoSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPsicologoOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return PerfilPsicologico.objects.all()
        return PerfilPsicologico.objects.filter(usuario=user)
