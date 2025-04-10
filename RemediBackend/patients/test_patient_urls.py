from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser
# Create your tests here.
class PatientUrlTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username= 'test', password = 'testpass', user_type = 'provider')
    def testPatDash(self):
        self.client.login(username = 'test', password = 'testpass')
        response = self.client.get(reverse('patient_dashboard'))
        self.assertEqual(response.status_code, 200)