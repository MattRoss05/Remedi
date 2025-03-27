from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class HomeUrlTest(TestCase):
    def testHome(self):
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)