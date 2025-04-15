from django.test import SimpleTestCase, TestCase
from .forms import AddPatient, AddPatientCustomUser
from users.forms import ProviderRegisterForm
from .models import Provider

class TestForm(TestCase):
    #test that AddPatient and AddPatientCustomUser forms are creating valid forms
    #aswell as if models are correctlly being instantiated
    def testValidData(self):
        #create a Provider user to tie to a test patient
        providerUserForm = ProviderRegisterForm(
            data = {
                'username': 'TestProvider', 'email': 'TProvider@gmail.com',
                'password1': 'securepass1', 'password2': 'securepass1'
            }
        )
        #save the from to create a provider user
        providerUser = providerUserForm.save()
        #use the provider user to create the provider model to be tied to partient
        #get_or_created creates a tuple, so it must be unpacked
        providerInstance, created = Provider.objects.get_or_create(user = providerUser)
        #create the patient form instance
        form1 = AddPatient(
            data = {
                'first': 'Luke', 'last': 'Skywalker'
            }
        )
        #assert the form is valid
        self.assertTrue(form1.is_valid())
        #create the patient user form instance
        form2 = AddPatientCustomUser(
            data = {
                'username': 'test', 'email': 'test@gmail.com', 
                'password1': 'testpassword', 'password2': 'testpassword'
            }
        )
        #assert the patient user form is valid
        self.assertTrue(form2.is_valid())
        #use save to create the user model
        userInstance = form2.save()

        #temporarily save current values in model
        patientInstance = form1.save(commit = False)
        #tie the Provider instance to the patient
        patientInstance.provider = providerInstance
        patientInstance.user = userInstance
        patientInstance.save()
        #assert that the user model for the patient was created
        self.assertIsNotNone(userInstance)
        #assert that the patient model for the patient was created
        self.assertIsNotNone(patientInstance)
        #query database for the saved patient Instance
        patientInstance.refresh_from_db()
        #assert that it is equal to the created Provider
        self.assertEqual(patientInstance.provider, providerInstance) 


    #test that empty fields cannot be submitted
    def testNoData(self):
        form = AddPatient(data = {})
        self.assertFalse(form.is_valid())