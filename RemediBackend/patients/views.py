from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from providers.models import Patient, Provider, Prescription, Report


# Create your views here.

def patient_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == 'patient':
        #render the patient dashbaord if logged in
        return render(request, 'patients/patientdashboard.html')
    else:
        #return to the landing page
        return redirect('welcome')
    
def view_medications(request):
    #if the user is not authenticated as a patient, redirect to the landing page
    if not request.user.is_authenticated or request.user.user_type == 'provider':
       return redirect('welcome')

    #pull meds
    meds = Prescription.objects.filter(patient = request.user.patient)
    #render the html files and pass the list of prescriptions
    return render(request, 'patients/viewmedications.html', {'meds': meds})


def log_confirmation(request, medication_id):
    #if the user isn't authenticated as a patient, redirect to the landing page
    if not request.user.is_authenticated or request.user.user_type == 'provider':
       return redirect('welcome')
    else:
        #if the form has been submitted
        if request.method == "POST":
            #get the associated prescription
            med = get_object_or_404(Prescription, id = medication_id)

            #build associated report object and tie the report tot the obtained prescription and patient model
            report = Report()

            report.prescription = med
            report.patient = request.user.patient
            report.save()

            #redirect to view medications
            return redirect('view_medications')
        else:
            #other wise, get the assoicated medication and render the html file
            med = get_object_or_404(Prescription, id = medication_id)
            return render(request, 'patients/logconfirmation.html', {'med': med})



    




