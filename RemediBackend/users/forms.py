#import forms from django so we can create new
#form fields
from django import forms
#import built in django UserCreationForm so we can
#extend it and maker our custom regristration form
from django.contrib.auth.forms import UserCreationForm
#import our CustomUser model so we can tel django
#that the database object made from this form is 
#of type CustomUser
from .models import CustomUser

#make a class, so we can make a custom UserCreationForm that
#extends UserCreationForm
class ProviderRegisterForm(UserCreationForm):
    #add an email field to the form
    email = forms.EmailField()
    class Meta:
        #a customuser object will be made from the form
        model = CustomUser
        # a CustoMuser will take in these fields from the from
        #(they are shown on the form that the user sees)
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    #only need to add this custom method because Django will automatically 
    #call it when form.is_valid() is called in views
    def clean_email(self):
        email = self.cleaned_data.get('email')

        #check if email already exists in the database
        if CustomUser.objects.filter(email = email).exists():
            # if i does, raise an error to be displayed to the user
            raise forms.ValidationError('This email is already registered. Please use a different one.')

        
        #if the email is valid thus far, return it
        return email
