from django.db import models
from django.contrib.auth.models import User
from .psicologo import Psicologo

class Cita(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]

    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas')
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    motivo = models.TextField()
    enlace_sesion = models.TextField(blank=True, null=True)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'citas'

    def __str__(self):
        return f"Cita: {self.paciente.username} con {self.psicologo.usuario.username} - {self.fecha} {self.hora}"
