from django.db import models
from users.models import CustomUser
# Create your models here.
class Provider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='patients')

    date_of_birth = models.DateField()
    address = models.TextField()
    medications_times = models.JSONField(default=dict)


    def __str__(self):
        return self.user.email