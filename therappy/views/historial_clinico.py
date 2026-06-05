from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from therappy.permissions import IsAdminOrPsicologoOrReadOnly
from therappy.models.historial_clinico import HistorialClinico
from therappy.serializers.historial_clinico import HistorialClinicoSerializer
from django.db.models import Q

class HistorialClinicoViewSet(viewsets.ModelViewSet):
    serializer_class = HistorialClinicoSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPsicologoOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return HistorialClinico.objects.all()
        return HistorialClinico.objects.filter(Q(paciente=user) | Q(psicologo__usuario=user))
