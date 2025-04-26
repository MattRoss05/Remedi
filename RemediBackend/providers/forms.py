from django import forms
from .models import Patient, Provider, CustomUser #accessing patient and provider models
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

class EditPatientCustomUser (forms.ModelForm):

    #specify email field
    email = forms.EmailField(required=True)
    
    class Meta:
        
        #every time we make a submission in this field, it should change customuser model
        model = CustomUser

        #this is for specifying the order that we want the fields to appear
        fields = [
            "username",
            "email",
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current = self.instance.email
        #check if email already exists in the database
        if email != current:
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
        
#form for the edit user view
class EditPatientForm(forms.ModelForm):
    #form will display first, last, and medication times
    class Meta:
        #Patient is the model being edited
        model = Patient

        fields = [
            'first', 'last', #'medications_times'
            ]
        #`these are texts that will be displayed next to the associated form`
        help_texts = {
            'first': 'Enter the patient\'s first name.',
            'last': 'Enter the patient\'s last name.',
            #medications_times': 'Medications and times should be entered in JSON format',
        }
#form for the change password view
class CustomPasswordChangeForm(PasswordChangeForm):
    #old padssword is not required
    old_password = None

    #make the new password field
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput,
        min_length=8,
        help_text="Password must be at least 8 characters long."
    )
    #make the matchting password field
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput,
        min_length=8,
        help_text="Enter the same password as above."
    )

    class Meta:
        # CustomUser is the model being edited
        model = CustomUser
        fields = [
            'new_password1', 
            'new_password2',
        ]
    #override clean_new_password2 method
    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')

        if password1 != password2:
            raise ValidationError("The two password fields must match.")
        
        return password2
    #override save method to include user
    def save(self, user):
        new_password = self.cleaned_data.get('new_password1')
        user.set_password(new_password)
        user.save()