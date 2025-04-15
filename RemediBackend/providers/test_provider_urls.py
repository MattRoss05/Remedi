from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser
# Create your tests here
class ProviderUrlTest(TestCase):
    #create a user object to simulate a user
    def setUp(self):
        self.user = CustomUser.objects.create_user(username= 'test', password = 'testpass', user_type = 'provider')
    def testProvDash(self):
        self.client.login(username = 'test', password = 'testpass')
        response = self.client.get(reverse('provider_dashboard'))
        self.assertEqual(response.status_code, 200)
    # test for if the add patient url was reached
    def testAddPatient(self):
        self.client.login(username = 'test' , password = 'testpass', user_type = 'provider')
        response = self.client.get(reverse('add_patient'))
        self.assertEqual(response.status_code, 200)