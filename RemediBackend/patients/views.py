from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from providers.models import Patient, Provider, Prescription, Report


# Create your views here.

def patient_dashboard(request):
    if request.user.is_authenticated or request.user.user_type == 'provider':
        #render the patient dashbaord if logged in
        return render(request, 'patients/patientdashboard.html')
    else:
        return redirect('welcome')
    
def view_medications(request):
    if not request.user.is_authenticated or request.user.user_type == 'provider':
       return redirect('welcome')

    #pull meds
    meds = Prescription.objects.filter(patient = request.user.patient)

    return render(request, 'patients/viewmedications.html', {'meds': meds})


def log_confirmation(request, medication_id):
    if not request.user.is_authenticated or request.user.user_type == 'provider':
       return redirect('welcome')
    else:
        if request.method == "POST":
            med = get_object_or_404(Prescription, id = medication_id)

            report = Report()

            report.prescription = med
            report.patient = request.user.patient
            report.save()
            return redirect('view_medications')
        else:
            med = get_object_or_404(Prescription, id = medication_id)
            return render(request, 'patients/logconfirmation.html', {'med': med})



    




