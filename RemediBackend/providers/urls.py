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
    path('change-prescriptions/<int:patient_id>/change', views.change_medications, name = 'change_medications'),
    #url path for add medication, include patient id in url
    path('add-prescription/<int:patient_id>/add', views.add_medication, name = 'add_medication'),
    #url path for edit medication, include patient id and medication id in url
    path('edit-prescription/<int:patient_id>/<int:medication_id>/edit', views.edit_medication, name = 'edit_medication'),
    #url path for delete medication, include patient id and medication id in url
    path('delete-prescription/<int:patient_id>/<int:medication_id>/delete', views.delete_medication, name = 'delete_medication'),
    #url path for view report include patient id url
    path('view-report/<int:patient_id>/add', views.view_reports, name = 'view_report'),

]