from django.urls import path
from . import views

urlpatterns = [
    #url path for the provider dashboard
    path('', views.provider_dashboard, name = 'provider_dashboard'),
    #url path for add patient
    path('add-patient', views.add_patient, name = 'add_patient'),
    #url for search patient
    path('search-patient', views.search_patient, name = 'search_patients'),
    #url for delete patient, include patient id in url
    path('delete-patient/<int:patient_id>/delete', views.delete_patient, name = 'delete_patient'),
    #url for edit patient, include patient id in the url
    path('edit-patient/<int:patient_id>/edit', views.edit_patient, name = 'edit_patient' ),
    #url for the change password, include patient id in the url
    path('change-password/<int:patient_id>/change', views.change_password, name = 'change_password' ),
    #url path for change medication, include patient id in url
    path('change-medications/<int:patient_id>/change', views.change_medications, name = 'change_medications' ),

]