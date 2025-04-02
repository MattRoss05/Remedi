#import models to make new model fields
from django.db import models
#import AbstractUser so Custom user can inherit all fiels of the
# built in django User
from django.contrib.auth.models import AbstractUser
# Create your models here.
#custom user model with and added user_type field
class CustomUser(AbstractUser):
    #touple of tuples for provider choices. second vield of each inner tuple is what will
    #show up on screen in forms
    USER_TYPE = (
        ('patient', 'Patient'),
        ('provider', 'Provider'),
    )

    #user_type field that is a choice field of maxx length 10 from the USER_TYPE tuple
    user_type = models.CharField(max_length=10, choices = USER_TYPE, default='provider')

    #helper methods to determine if a user is a patient or provider.
    def is_patient(self):
        return self.user_type == 'patient'
    
    def is_provider(self):
        return self.user_type == 'provider'
