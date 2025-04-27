from django.contrib import admin
from .models import Patient, Provider, Report, Prescription
# Register your models here.
admin.site.register(Provider)
admin.site.register(Patient)
admin.site.register(Report)
admin.site.register(Prescription)