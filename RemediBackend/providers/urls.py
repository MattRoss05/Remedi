from django.urls import path
from . import views

urlpatterns = [
    path('', views.provider_dashboard, name = 'provider_dashboard'),
    path('add-patient', views.add_patient, name = 'add_patient')
]