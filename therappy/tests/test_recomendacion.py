from rest_framework.test import APITestCase
from rest_framework import status
from therappy.models.recomendacion import Recomendacion
from .helpers import create_user, get_auth_client

class RecomendacionTests(APITestCase):
    def setUp(self):
        self.user = create_user('testuser', 'test@example.com', 'password123')
        self.client = get_auth_client(self.user)
        self.url = '/api/recomendaciones/'
        self.recomendacion = Recomendacion.objects.create(
            usuario=self.user,
            titulo='Meditar 10 mins',
            descripcion='Medita',
            tipo='meditación'
        )

    def test_list_recomendaciones(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
