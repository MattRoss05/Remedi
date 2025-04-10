from django.urls import path
from . import views

urlpatterns = [
    path('', views.provider_dashboard, name = 'provider_dashboard'),
    path('add-patient', views.add_patient, name = 'add_patient'),
    path('search-patient', views.search_patient, name = 'search_patients'),
    path('delete-patient/<int:patient_id>/delete', views.delete_patient, name = 'delete_patient'),
    path('edit-patient/<int:patient_id>/edit', views.edit_patient, name = 'edit_patient' ),
     path('change-password/<int:patient_id>/change', views.change_password, name = 'change_password' ),
]