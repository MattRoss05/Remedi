from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('patient', 'Patient'),
        ('provider', 'Provider'),
    )
    user_type = models.CharField(max_length=10, choices = USER_TYPE, default='provider')

    def is_patient(self):
        return self.user_type == 'patient'
    
    def is_provider(self):
        return self.user_type == 'provider'
    
