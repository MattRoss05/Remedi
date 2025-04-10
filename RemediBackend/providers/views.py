from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AddPatientCustomUser, AddPatient
from .models import Provider, Patient
from django.db.models import Q

# Create your views here.
def provider_dashboard(request):
    if request.user.is_authenticated:
        #render the provider dashboard, can only be accessed if logged in
        return render(request, 'providers/providerdashboard.html')
    else:
        return redirect('welcome')
    
def add_patient(request):
    #upon hitting submit button for filled form
    if not request.user.is_authenticated:
        return redirect('welcome')
    
    if request.method=="POST":
        #AddPatient and AddPatientCustomUser form
        patientForm = AddPatient(request.POST)
        userForm = AddPatientCustomUser(request.POST)
        if patientForm.is_valid() and userForm.is_valid():
            #save customuser
            user = userForm.save()
             #save patient but we not done yet
            patient = patientForm.save(commit=False)
            #create the provider representing the logged in provider to attach to patient
            provider = Provider.objects.get(user=request.user)
            #attach provider to patient
            patient.provider = provider
            #then we wanna map this patient to their relevant user model
            patient.user = user
            #nowwwww we save
            patient.save()
            #take me home boys
            return redirect('provider_dashboard')
        #otherwise give the provider a blank form
    else:
        patientForm = AddPatient()
        userForm = AddPatientCustomUser()
                
        return render(request, 'providers/addpatient.html', {'patientForm': patientForm, 'userForm': userForm})
    
def search_patient(request):
    if not request.user.is_authenticated or request.user.user_type == 'patient':
       return redirect('welcome')
    query = request.GET.get('q', '')
    if query:
        patients = Patient.objects.filter(Q(first__icontains = query)|Q(last__icontains = query), provider = request.user.provider)

                                          
    else:
        patients = Patient.objects.filter(provider = request.user.provider)
    return render(request, 'providers/searchpatients.html', {'patients': patients, 'query': query})


def delete_patient(request, patient_id):
    if not request.user.is_authenticated and request.user.user_type == 'patient':
       return redirect('welcome')
    patient  = get_object_or_404(Patient, id = patient_id)

    if request.method == "POST":
        patient.delete()
        return redirect('search_patients')
    
    else:
        return render(request, 'providers/confirmdelete.html', {'patient': patient})





