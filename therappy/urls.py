from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from therappy.views.health import health_check
from therappy.views.auth import CustomTokenView, RegisterView, LogoutView
from therappy.views.user import UserViewSet
from therappy.views.psicologo import PsicologoViewSet
from therappy.views.cita import CitaViewSet
from therappy.views.historial_clinico import HistorialClinicoViewSet
from therappy.views.emocion import EmocionViewSet
from therappy.views.recomendacion import RecomendacionViewSet
from therappy.views.perfil_psicologico import PerfilPsicologicoViewSet
from therappy.views.chat import ChatViewSet, MensajeViewSet
from therappy.views.portal_admin import PortalAdminViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'psicologos', PsicologoViewSet, basename='psicologo')
router.register(r'citas', CitaViewSet, basename='cita')
router.register(r'historiales', HistorialClinicoViewSet, basename='historial')
router.register(r'emociones', EmocionViewSet, basename='emocion')
router.register(r'recomendaciones', RecomendacionViewSet, basename='recomendacion')
router.register(r'perfiles-psicologicos', PerfilPsicologicoViewSet, basename='perfil-psicologico')
router.register(r'chats', ChatViewSet, basename='chat')
router.register(r'mensajes', MensajeViewSet, basename='mensaje')
router.register(r'portal-admin', PortalAdminViewSet, basename='portal-admin')

urlpatterns = [
    path('health/', health_check, name='health-check'),
    path('auth/login/', CustomTokenView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]