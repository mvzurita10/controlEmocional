from rest_framework import viewsets
from therappy.models.emocion import Emocion
from therappy.serializers.emocion import EmocionSerializer

class EmocionViewSet(viewsets.ModelViewSet):
    queryset = Emocion.objects.all()
    serializer_class = EmocionSerializer
