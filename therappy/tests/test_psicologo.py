from rest_framework.test import APITestCase
from rest_framework import status
from therappy.models.psicologo import Psicologo
from .helpers import create_user, get_auth_client

class PsicologoTests(APITestCase):
    def setUp(self):
        self.user = create_user('psicologo1', 'psi@example.com', 'password123')
        self.client = get_auth_client(self.user)
        self.url = '/api/psicologos/'
        self.psicologo = Psicologo.objects.create(
            usuario=self.user,
            especialidad='Clínica',
            descripcion='Test',
            experiencia=5,
            universidad='Test Univ',
            licencia_profesional='12345'
        )

    def test_list_psicologos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
