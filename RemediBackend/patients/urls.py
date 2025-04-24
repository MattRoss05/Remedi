from django.urls import path
from . import views

urlpatterns = [
    #url path for patient dashboard
    path('', views.patient_dashboard, name = 'patient_dashboard'),
    #url path for medication view
    path('view-medications', views.view_medications, name = 'view_medications'),
    #url path for medication log
    path('log-medications', views.log_medications, name = 'log_medications'),
]