from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class ProviderUrlTest(TestCase):
    def testProvDash(self):
        response = self.client.get(reverse('provider_dashboard'))
        self.assertEqual(response.status_code, 200)
