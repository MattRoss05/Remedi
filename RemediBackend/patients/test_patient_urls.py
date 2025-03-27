from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class PatientUrlTest(TestCase):
    def testPatDash(self):
        response = self.client.get(reverse('patient_dashboard'))
        self.assertEqual(response.status_code, 200)