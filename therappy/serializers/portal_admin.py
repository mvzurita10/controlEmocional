from rest_framework import serializers
from therappy.models.portal_admin import PortalAdmin

class PortalAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalAdmin
        fields = '__all__'
