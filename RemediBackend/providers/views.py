
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AddPatientCustomUser, AddPatient, EditPatientForm, EditPatientCustomUser, CustomPasswordChangeForm, EditMedicationForm
from .models import Provider, Patient, Prescription
from django.db.models import Q

# Create your views here.
def provider_dashboard(request):
    if request.user.is_authenticated or request.user.user_type == 'patient':
        #render the provider dashboard, can only be accessed if logged in
        return render(request, 'providers/providerdashboard.html')
    else:
        return redirect('welcome')
    
def add_patient(request):
    #upon hitting submit button for filled form
    if not request.user.is_authenticated or request.user.user_type == 'patient':
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
    #if the user isnt authenticated as a provider, redirect to the welcome page
    if not request.user.is_authenticated or request.user.user_type == 'patient':
       return redirect('welcome')
    #get the query from the user
    query = request.GET.get('q', '')
    #if the query is not blank
    if query:
        #get a list of matching patients based of either the first or last name, for now, you cannot use both
        patients = Patient.objects.filter(Q(first__icontains = query)|Q(last__icontains = query), provider = request.user.provider)

    #if the quuery is blank                                     
    else:
        #get all patients related to the authenticated provider
        patients = Patient.objects.filter(provider = request.user.provider)
    #render the html file with the acquired list of patients
    return render(request, 'providers/searchpatients.html', {'patients': patients, 'query': query})


def delete_patient(request, patient_id):
    #if the user is not authenitcated as a provider
    if not request.user.is_authenticated or request.user.user_type == 'patient':
       #redirect to the welcome page.
       return redirect('welcome')
    #obtain the patient to delete based off of id and the proider authenticated
    patient  = get_object_or_404(Patient, id = patient_id, provider = request.user.provider)

    #if the form has been submitted
    if request.method == "POST":
        #delete the user associated with the patient, the patient model associated with the user will be by CASCADE
        patient.user.delete()
        #redirect to search patients
        return redirect('search_patients')
    
    else:
        #if the form has not been submitted, render the html file and pass the patient they can be displayed on the screen
        return render(request, 'providers/confirmdelete.html', {'patient': patient})


def edit_patient(request, patient_id):
    #if the user is not authenitcated as a provider
    if not request.user.is_authenticated or request.user.user_type == 'patient':
       #redirect to the welcome page.
       return redirect('welcome')
     #obtain the patient to edit based off of id and the proider authenticated
    patient = get_object_or_404(Patient, id = patient_id, provider = request.user.provider)

    # if the form has been submitted
    if request.method == "POST":
        #intialize forms with the data provided from the user and the instance being changed
        editUserForm = EditPatientCustomUser(request.POST, instance = patient.user)
        editForm = EditPatientForm(request.POST, instance = patient)
        #error prints from debugging
        print(editForm.errors)
        print(editUserForm.errors)
        #if the forms are valid
        if editForm.is_valid() and editUserForm.is_valid():
            # save them and redirect to search patients
            editForm.save()
            editUserForm.save()
            return redirect('search_patients')
        else:
            #allows validation errors to be displayed
            return render(request, 'providers/editpatient.html', {'editForm': editForm, 'patient': patient, 'editUserForm': editUserForm})
        
    else:
        #provide the forms to the user with existing information in thenm, allows for easier editing
        editForm = EditPatientForm(instance = patient)
        editUserForm = EditPatientCustomUser(instance = patient.user)
        return render(request, 'providers/editpatient.html', {'editForm': editForm, 'patient': patient, 'editUserForm': editUserForm})



def change_password(request, patient_id):
    #if the user is not authenitcated as a provider
    if not request.user.is_authenticated or request.user.user_type == 'patient':
       #redirect to welcome
       return redirect('welcome')
    #obtain the patient to edit based off of id and the proider authenticated
    patient = get_object_or_404(Patient, id = patient_id, provider = request.user.provider)

    #if the form has been submitted
    if request.method == "POST":
        #initialize th form with the data provided and the user to be edited
        changepasswordform = CustomPasswordChangeForm(user=patient.user,data= request.POST)
        #if the form is valid
        if changepasswordform.is_valid():
            #save the forms and redirect to editpatient page of the user just edited
            changepasswordform.save(user = patient.user)
            return redirect('edit_patient', patient_id = patient.id)
    else:
        #otherwise provide blank forms with the user to be edited.
        changepasswordform = CustomPasswordChangeForm(user = patient.user)
        return render(request, 'providers/changepassword.html', {'patient':patient, 'changepasswordform':changepasswordform})

def change_medications(request, patient_id):
#if the user is not authenitcated as a provider
    if not request.user.is_authenticated or request.user.user_type == 'patient':
       #redirect to welcome
       return redirect('welcome')
    
    patient = get_object_or_404(Patient, id = patient_id, provider = request.user.provider) 
    precriptions = Prescription.objects.filter(patient = patient)
    
    return render(request, 'providers/changemeds.html', {'patient': patient, 'prescriptions': precriptions})



def add_medication(request, patient_id):
     #upon hitting submit button for filled form
    if not request.user.is_authenticated or request.user.user_type == 'patient':
        return redirect('welcome')
    patient = get_object_or_404(Patient, id = patient_id, provider = request.user.provider)
    if request.method=="POST":
        patient = get_object_or_404(Patient, id = patient_id, provider = request.user.provider)
        medicationForm = EditMedicationForm(request.POST)
        if medicationForm.is_valid():
       
            medication = medicationForm.save(commit=False)
           
            patient = get_object_or_404(Patient, id = patient_id, provider = request.user.provider)
            
            medication.patient = patient
           
            medication.save()
            
            return redirect('change_medications', patient_id = patient_id)
      
    else:
        medicationForm = EditMedicationForm()
             
    return render(request, 'providers/addmedication.html', {'medForm': medicationForm, 'patient':patient})


def edit_medication(request, patient_id, medication_id):
  #upon hitting submit button for filled form
    if not request.user.is_authenticated or request.user.user_type == 'patient':
        return redirect('welcome')
    patient = get_object_or_404(Patient, id = patient_id, provider = request.user.provider)
    medication = get_object_or_404(Prescription, id = medication_id, patient = patient)
    if request.method=="POST":
        
        medicationForm = EditMedicationForm(request.POST, instance= medication)
        if medicationForm.is_valid():
       
            medication = medicationForm.save(commit=False)
           
            medication.save()
            
            return redirect('change_medications',patient_id = patient_id)
      
    else:
        medicationForm = EditMedicationForm(instance = medication)
                
    return render(request, 'providers/editmedication.html', {'medForm': medicationForm, 'patient': patient, 'medication': medication}) 
def delete_medication(request, patient_id, medication_id):
    #if the user is not authenitcated as a provider
    if not request.user.is_authenticated or request.user.user_type == 'patient':
       #redirect to the welcome page.
       return redirect('welcome')
    #obtain the patient to delete based off of id and the proider authenticated
    patient  = get_object_or_404(Patient, id = patient_id, provider = request.user.provider)
    med = get_object_or_404(Prescription, id = medication_id, patient = patient)

    #if the form has been submitted
    if request.method == "POST":
        #delete the user associated with the patient, the patient model associated with the user will be by CASCADE
        med.delete()
        #redirect to search patients
        return redirect('change_medications', patient_id = patient_id)
    
    else:
        #if the form has not been submitted, render the html file and pass the patient they can be displayed on the screen
        return render(request, 'providers/confirmdeletemed.html', {'patient': patient, 'medication':med}) 
    
    
    
