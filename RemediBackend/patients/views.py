from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def patient_dashboard(request):
    if request.user.is_authenticated:
        #render the patient dashbaord if logged in
        return render(request, 'patients/patientdashboard.html')
    else:
        return redirect('welcome')
    
def view_medications(request):
    if request.user.is_authenticated:
        #render the medication view if logged in as patient
        return render(request, 'patients/viewmedications.html')
    else:
        return redirect('welcome')
    

def log_medications(request):
    if request.user.is_authenticated:
        #render the log medication view if logged in as patient
        return render(request, 'patients/logmedications.html')
    else:
        return redirect('welcome')


