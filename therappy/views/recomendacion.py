from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from therappy.permissions import IsAdminOrPsicologoOrReadOnly
from therappy.models.recomendacion import Recomendacion
from therappy.serializers.recomendacion import RecomendacionSerializer
from django.db.models import Q

class RecomendacionViewSet(viewsets.ModelViewSet):
    serializer_class = RecomendacionSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPsicologoOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Recomendacion.objects.all()
        return Recomendacion.objects.filter(usuario=user)
