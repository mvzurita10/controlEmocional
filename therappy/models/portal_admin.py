from django.db import models
from django.contrib.auth.models import User

class PortalAdmin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acciones_admin')
    accion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'portal_admin'

    def __str__(self):
        return f"Admin: {self.admin.username} - {self.accion} ({self.fecha.date()})"
