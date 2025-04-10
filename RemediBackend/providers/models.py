from django.db import models
from users.models import CustomUser
# Create your models here.
class Provider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    


class Patient(models.Model):
    #maps our patient to a custom user model
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #first and last name fields; this is what we use to search a patient
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)

    medications_times = models.JSONField(default=dict)
    #the provider who intoduced this patient is saved here
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.user.email