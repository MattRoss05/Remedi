from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class PatientUrlTest(TestCase):
    def testDash(self):
        response = self.client.get(reverse('provider_dashboard'))
        self.assertEqual(response.status_code, 200)
