from django import forms
from .models import Patient, Provider, CustomUser #accessing patient and provider models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput

#this class is SPECIFICALLY for mapping fields to custom user (ie email user and pass)
class AddPatientCustomUser (UserCreationForm):

    #specify email field
    email = forms.EmailField(required=True)
    
    class Meta:
        
        #every time we make a submission in this field, it should change customuser model
        model = CustomUser

        #this is for specifying the order that we want the fields to appear
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        #check if email already exists in the database
        if CustomUser.objects.filter(email = email).exists():
            # if i does, raise an error to be displayed to the user
            raise forms.ValidationError('This email is already registered. Please use a different one.')

            
            #if the email is valid thus far, return it
        return email
            
    def save(self, commit = True):
        user = super().save(commit = False)
        user.user_type = 'patient'
        if commit:
            user.save()
        return user
        

#this class is SPECIFICALLY for mapping fields to patient model (ie first and last name)
class AddPatient(forms.ModelForm):

    #specify first and last name fields
    first = forms.CharField(required=True, max_length=30)
    last = forms.CharField(required=True, max_length=30)

    class Meta:

        #this time we want to update our Patient model
        model = Patient

        #specify order that each field pops up in
        fields = [
            "first",
            "last"
        ]