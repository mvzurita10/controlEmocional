from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from therappy.permissions import IsAdminOrPsicologoOrCanCreateCertain
from therappy.models.cita import Cita
from therappy.serializers.cita import CitaSerializer
from django.db.models import Q

class CitaViewSet(viewsets.ModelViewSet):
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPsicologoOrCanCreateCertain]
    search_fields = ['motivo', 'estado']
    filterset_fields = ['estado', 'fecha']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Cita.objects.all().order_by('-id')
        return Cita.objects.filter(Q(paciente=user) | Q(psicologo__usuario=user)).order_by('-id')
