from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class UserUrlTest(TestCase):
    def testRegister(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def testRedirect(self):
        response = self.client.get(reverse('role_based_redirect'))
        self.assertEqual(response.status_code, 302)

