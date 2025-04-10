from django.urls import path
from . import views

urlpatterns = [
    path('', views.provider_dashboard, name = 'provider_dashboard'),
    path('add-patient', views.add_patient, name = 'add_patient'),
    path('search-patient', views.search_patient, name = 'search_patients'),
    path('delete-patient/<int:patient_id>/delete', views.delete_patient, name = 'delete_patient')
]