from django.db import models
from django.contrib.auth.models import User

class Psicologo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='psicologo')
    especialidad = models.CharField(max_length=100)
    descripcion = models.TextField()
    experiencia = models.IntegerField(help_text="Años de experiencia")
    universidad = models.CharField(max_length=150)
    licencia_profesional = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    valoracion = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    class Meta:
        db_table = 'psicologos'

    def __str__(self):
        return f"Psicólogo: {self.usuario.get_full_name()} - {self.especialidad}"
