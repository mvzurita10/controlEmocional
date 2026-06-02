from rest_framework.test import APITestCase
from rest_framework import status
from therappy.models.perfil_psicologico import PerfilPsicologico
from .helpers import create_user, get_auth_client

class PerfilPsicologicoTests(APITestCase):
    def setUp(self):
        self.user = create_user('testuser', 'test@example.com', 'password123')
        self.client = get_auth_client(self.user)
        self.url = '/api/perfiles-psicologicos/'
        self.perfil = PerfilPsicologico.objects.create(
            usuario=self.user,
            nivel_estres=5,
            nivel_ansiedad=6,
            nivel_depresion=2,
            personalidad='Introvertido'
        )

    def test_list_perfiles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
