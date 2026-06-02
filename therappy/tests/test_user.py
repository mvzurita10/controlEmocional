from rest_framework.test import APITestCase
from rest_framework import status
from .helpers import create_user, get_auth_client

class UserTests(APITestCase):
    def setUp(self):
        self.user = create_user('testuser', 'test@example.com', 'password123')
        self.client = get_auth_client(self.user)
        self.me_url = '/api/users/me/'

    def test_get_user_profile(self):
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
