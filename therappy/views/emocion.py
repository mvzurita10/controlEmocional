from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from therappy.permissions import IsAdminOrPsicologoOrCanCreateCertain
from therappy.models.emocion import Emocion
from therappy.serializers.emocion import EmocionSerializer

class EmocionViewSet(viewsets.ModelViewSet):
    serializer_class = EmocionSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPsicologoOrCanCreateCertain]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Emocion.objects.all()
        return Emocion.objects.filter(usuario=user)
