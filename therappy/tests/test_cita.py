from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from therappy.models.psicologo import Psicologo
from therappy.models.cita import Cita
from .helpers import create_user, get_auth_client
import datetime

class CitaTests(APITestCase):
    def setUp(self):
        self.paciente = create_user('paciente1', 'pac@example.com', 'password123')
        self.psicologo_user = create_user('psi1', 'psi1@example.com', 'password123')
        self.psicologo = Psicologo.objects.create(
            usuario=self.psicologo_user, especialidad='Clínica', descripcion='Test', experiencia=5, universidad='Test Univ', licencia_profesional='12345'
        )
        self.client = get_auth_client(self.paciente)
        self.url = '/api/citas/'
        self.cita = Cita.objects.create(
            paciente=self.paciente,
            psicologo=self.psicologo,
            fecha=datetime.date.today(),
            hora=datetime.time(10, 0),
            motivo='Consulta inicial'
        )

    def test_list_citas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
