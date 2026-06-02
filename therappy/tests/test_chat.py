from rest_framework.test import APITestCase
from rest_framework import status
from therappy.models.psicologo import Psicologo
from therappy.models.chat import Chat, Mensaje
from .helpers import create_user, get_auth_client

class ChatTests(APITestCase):
    def setUp(self):
        self.paciente = create_user('paciente1', 'pac@example.com', 'password123')
        self.psicologo_user = create_user('psi1', 'psi1@example.com', 'password123')
        self.psicologo = Psicologo.objects.create(
            usuario=self.psicologo_user, especialidad='Clínica', descripcion='Test', experiencia=5, universidad='Test', licencia_profesional='12345'
        )
        self.client = get_auth_client(self.paciente)
        self.chat_url = '/api/chats/'
        self.mensaje_url = '/api/mensajes/'
        
        self.chat = Chat.objects.create(paciente=self.paciente, psicologo=self.psicologo)
        self.mensaje = Mensaje.objects.create(chat=self.chat, remitente=self.paciente, mensaje='Hola')

    def test_list_chats(self):
        response = self.client.get(self.chat_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_list_mensajes(self):
        response = self.client.get(self.mensaje_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
