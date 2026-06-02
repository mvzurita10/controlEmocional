from rest_framework import viewsets
from therappy.models.recomendacion import Recomendacion
from therappy.serializers.recomendacion import RecomendacionSerializer

class RecomendacionViewSet(viewsets.ModelViewSet):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer
