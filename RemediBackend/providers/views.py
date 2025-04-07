from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AddPatientCustomUser, AddPatient
from .models import Provider

# Create your views here.
def provider_dashboard(request):
    if request.user.is_authenticated:
        #render the provider dashboard, can only be accessed if logged in
        return render(request, 'providers/providerdashboard.html')
    else:
        return redirect('welcome')
    
def add_patient(request):
    #upon hitting submit button for filled form
    if request.method=="POST":
        #AddPatient and AddPatientCustomUser form
        patientForm = AddPatient(request.POST)
        userForm = AddPatientCustomUser(request.POST)
        if patientForm.is_valid() and userForm.is_valid():
            #save customuser
            user = userForm.save()
            #save patient but we not done yet
            patient = patientForm.save(commit=False)
            #then we wanna map this patient to their relevant user model
            patient.user = user
            #nowwwww we save
            patient.save()
            #take me home boys
            return redirect('providers/providerdashboard.html')
    #otherwise give the provider a blank form
    else:
        patientForm = AddPatient()
        userForm = AddPatientCustomUser()
            
    return render(request, 'providers/addpatient.html')