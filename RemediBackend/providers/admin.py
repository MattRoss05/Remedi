from django.contrib import admin
from .models import Patient, Provider
# Register your models here.
admin.site.register(Provider)
admin.site.register(Patient)