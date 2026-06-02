from django.db import models
from django.contrib.auth.models import User

class Recomendacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recomendaciones')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'recomendaciones'

    def __str__(self):
        return f"Recomendación: {self.titulo} ({self.tipo})"
