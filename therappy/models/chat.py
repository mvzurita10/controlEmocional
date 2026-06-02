from django.db import models
from django.contrib.auth.models import User
from .psicologo import Psicologo

class Chat(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, related_name='chats')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chats'

    def __str__(self):
        return f"Chat: {self.paciente.username} - {self.psicologo.usuario.username}"

class Mensaje(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='mensajes')
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    enviado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mensajes'

    def __str__(self):
        return f"Mensaje de {self.remitente.username} en Chat {self.chat.id}"
