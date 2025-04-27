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
    #Choices for Day
    DAY_CHOICES = [
        ("MONDAY", "MONDAY"),
        ("TUESDAY", "TUESDAY"),
        ("WEDNESDAY","WEDNESDAY"),
        ("THURSDAY","THURSDAY"),
        ("FRIDAY","FRIDAY"),
        ("SATURDAY","SATURDAY"),
        ("SUNDAY","SUNDAY"),
    ]
    #Choices for Hour
    HOUR_CHOICES = [
        (1, 1),
        (2, 2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
        (11,11),
        (12,12),
    ]
    #Choices for min
    MIN_CHOICES = [
        (00, 00),
        (15, 15),
        (30, 30),
        (45, 45)
    ]

    #Choices for Meridiem
    MERIDIEM_CHOICES = [
        ("AM", "AM"),
        ("PM", "PM")
    ]
    
    #map our prescription to a patient model
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name = 'prescriptions')
    #med, day, and time params
    med = models.CharField(max_length=50)
    day = models.CharField(max_length = 9, choices = DAY_CHOICES)
    hour = models.IntegerField(choices = HOUR_CHOICES)
    min = models.IntegerField(choices = MIN_CHOICES)
    meridiem = models.CharField( max_length= 2, choices = MERIDIEM_CHOICES)
    

    def __str__(self):
        return self.med

    
class Report(models.Model):
    #map to related prescription and patient
    prescription = models.OneToOneField(Prescription, on_delete=models.SET_NULL, related_name='reports', null = True, blank = True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reports')
    #tells us when they took the medication

    #snapshot of prescription
    logged_time = models.DateTimeField(auto_now_add=True)

    med = models.CharField(max_length=50)
    day = models.CharField(max_length=9)
    hour = models.IntegerField(default = 12)
    min = models.IntegerField(default = 15)
    meridiem = models.CharField(max_length=2)


    def __str__(self):
        return f"Report for {self.med} on {self.logged_time}"
