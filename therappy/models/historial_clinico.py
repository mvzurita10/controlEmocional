from django.db import models
from django.contrib.auth.models import User
from .psicologo import Psicologo

class HistorialClinico(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historiales')
    psicologo = models.ForeignKey(Psicologo, on_delete=models.SET_NULL, null=True, related_name='historiales_creados')
    diagnostico = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    tratamiento = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historial_clinico'

    def __str__(self):
        return f"Historial de {self.paciente.username} - {self.fecha_registro.date()}"
