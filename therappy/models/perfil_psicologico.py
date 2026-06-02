from django.db import models
from django.contrib.auth.models import User

class PerfilPsicologico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_psicologico')
    nivel_estres = models.IntegerField(default=0)
    nivel_ansiedad = models.IntegerField(default=0)
    nivel_depresion = models.IntegerField(default=0)
    personalidad = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'perfil_psicologico'

    def __str__(self):
        return f"Perfil Psicológico de {self.usuario.username}"
