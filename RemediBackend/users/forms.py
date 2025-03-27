from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from email_validator import validate_email, EmailNotValidError, CHECK_DELIVERABILITY

class ProviderRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    #only need to add this custom method because Django will automatically fall it when form.is_valid() is called in views
    def clean_email(self):
        email = self.cleaned_data.get('email')

        #check if email already exists in the database
        if CustomUser.objects.filter(email = email).exists():
            raise forms.ValidationError('This email is already registered. Please use a different one.')

        

        return email
