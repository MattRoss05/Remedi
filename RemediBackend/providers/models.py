from django.db import models
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CustomUser
import datetime

# Create your models here.
class Provider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    

# Create your models here.
class Patient(models.Model):
    #maps our patient to a custom user model
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #first and last name fields; this is what we use to search a patient
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)

    #the provider who intoduced this patient is saved here
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.user.email
    
class Prescription(models.Model):
    DAY_CHOICES = [
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY","Wednesday"),
        ("THURSDAY","Thursday"),
        ("FRIDAY","Friday"),
        ("SATURDAY","Saturday"),
        ("SUNDAY","Sunday"),
    ]

    HOUR_CHOICES = [
        ("one", 1),
        ("two", 2),
        ("three",3),
        ("four",4),
        ("five",5),
        ("six",6),
        ("seven",7),
        ("eight",8),
        ("nine",9),
        ("ten",10),
        ("eleven",11),
        ("twelve",12),
        
    ]

    MIN_CHOICES = [
        ("zero", 00),
        ("fifteen", 15),
        ("thirty", 30),
        ("fortyfive", 45)
    ]


    MERIDIEM_CHOICES = [
        ("AM", "am"),
        ("PM", "pm")
    ]
    
    #map our prescription to a patient model
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name = 'prescriptions')
    #med, day, and time params
    med = models.CharField(max_length=50)
    day = models.CharField(max_length = 9, choices = DAY_CHOICES, default = "MONDAY")
    hour = models.IntegerField(choices = HOUR_CHOICES, default = "one")
    min = models.IntegerField(choices = MIN_CHOICES, default = "zero")
    meridiem = models.CharField( max_length= 2, choices = MERIDIEM_CHOICES, default = "AM")
    

    def __str__(self):
        return self.med

    
