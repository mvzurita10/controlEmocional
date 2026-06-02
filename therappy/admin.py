from django.contrib import admin
from .models.psicologo import Psicologo
from .models.cita import Cita
from .models.historial_clinico import HistorialClinico
from .models.emocion import Emocion
from .models.recomendacion import Recomendacion
from .models.perfil_psicologico import PerfilPsicologico
from .models.chat import Chat, Mensaje
from .models.portal_admin import PortalAdmin

admin.site.register(Psicologo)
admin.site.register(Cita)
admin.site.register(HistorialClinico)
admin.site.register(Emocion)
admin.site.register(Recomendacion)
admin.site.register(PerfilPsicologico)
admin.site.register(Chat)
admin.site.register(Mensaje)
admin.site.register(PortalAdmin)
