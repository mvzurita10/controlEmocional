from rest_framework.test import APITestCase
from rest_framework import status
from therappy.models.emocion import Emocion
from .helpers import create_user, get_auth_client

class EmocionTests(APITestCase):
    def setUp(self):
        self.user = create_user('testuser', 'test@example.com', 'password123')
        self.client = get_auth_client(self.user)
        self.url = '/api/emociones/'
        self.emocion = Emocion.objects.create(
            usuario=self.user,
            emocion='felicidad',
            intensidad=8,
            nota='Buen día'
        )

    def test_list_emociones(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
