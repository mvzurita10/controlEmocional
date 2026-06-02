from rest_framework import viewsets
from therappy.models.chat import Chat, Mensaje
from therappy.serializers.chat import ChatSerializer, MensajeSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
