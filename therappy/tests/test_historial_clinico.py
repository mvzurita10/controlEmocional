from rest_framework.test import APITestCase
from rest_framework import status
from therappy.models.psicologo import Psicologo
from therappy.models.historial_clinico import HistorialClinico
from .helpers import create_user, get_auth_client

class HistorialClinicoTests(APITestCase):
    def setUp(self):
        self.paciente = create_user('paciente1', 'pac@example.com', 'password123')
        self.psicologo_user = create_user('psi1', 'psi1@example.com', 'password123')
        self.psicologo = Psicologo.objects.create(
            usuario=self.psicologo_user, especialidad='Clínica', descripcion='Test', experiencia=5, universidad='Test Univ', licencia_profesional='12345'
        )
        self.client = get_auth_client(self.psicologo_user)
        self.url = '/api/historiales/'
        self.historial = HistorialClinico.objects.create(
            paciente=self.paciente,
            psicologo=self.psicologo,
            diagnostico='Ansiedad leve',
            tratamiento='Terapia cognitivo-conductual'
        )

    def test_list_historiales(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
