from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Emocion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emociones')
    emocion = models.CharField(max_length=50)
    intensidad = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    nota = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'emociones'

    def __str__(self):
        return f"{self.emocion} ({self.intensidad}/10) - {self.usuario.username}"
