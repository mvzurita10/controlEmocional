from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from therappy.models.portal_admin import PortalAdmin
from therappy.serializers.portal_admin import PortalAdminSerializer

class PortalAdminViewSet(viewsets.ModelViewSet):
    queryset = PortalAdmin.objects.all().order_by('-id')
    serializer_class = PortalAdminSerializer
    permission_classes = [IsAdminUser]
