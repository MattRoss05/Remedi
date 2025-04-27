from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from providers.models import Patient, Provider, Prescription

# Create your views here.

def patient_dashboard(request):
    if request.user.is_authenticated:
        #render the patient dashbaord if logged in
        return render(request, 'patients/patientdashboard.html')
    else:
        return redirect('welcome')
    
def view_medications(request):
    if not request.user.is_authenticated or request.user.user_type == 'provider':
       return redirect('welcome')

    #pull meds
    meds = Prescription.objects.filter(pateint = request.user.patient)

    return render(request, 'patients/viewmedications.html', {'meds': meds})
    




