from rest_framework.test import APITestCase
from rest_framework import status
from therappy.models.portal_admin import PortalAdmin
from .helpers import create_user, get_auth_client

class PortalAdminTests(APITestCase):
    def setUp(self):
        self.admin = create_user('admin_test', 'admin@example.com', 'password123')
        self.admin.is_staff = True
        self.admin.save()
        self.client = get_auth_client(self.admin)
        self.url = '/api/portal-admin/'
        self.portal = PortalAdmin.objects.create(
            admin=self.admin,
            accion='Revisión de logs',
            descripcion='Test desc'
        )

    def test_list_portal_admin(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
