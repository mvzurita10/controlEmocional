from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from therappy.permissions import IsAdminOrPsicologoOrCanCreateCertain
from therappy.models.chat import Chat, Mensaje
from therappy.serializers.chat import ChatSerializer, MensajeSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPsicologoOrCanCreateCertain]

class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrPsicologoOrCanCreateCertain]
