#import render and redirect to show html files
from django.shortcuts import render, redirect
#import our ProviderRegisterForM
from .forms import ProviderRegisterForm
#import login_required to allow login dependent redirect when
#logging in on the login page
from django.contrib.auth.decorators import login_required





# Create your views here.

#view for the register page
def register_page(request):
    # if the request method is POST, this means a form is being submitted
    if request.method == "POST":
        #create a form object using the submitted form as a parameter in the constructor
        form = ProviderRegisterForm(request.POST)
        #if the form is a valid form
        if form.is_valid():
            #save the form to the database
            form.save()
            #redirect to the landing page
            return redirect('welcome')
    else:
        #otherwise if no form has been submitted
        #make a blank form
        form = ProviderRegisterForm()
        #display the html file with a blank form to the user
    return render(request, 'users/register.html', {"form": form})
#login based redirect method
#must be logged in to access this view
@login_required
def role_based_redirect(request):
    #if the user associated with the request is of user_type = provider
    if request.user.is_provider():
        #redirect them to the provider dashboard
        return redirect('provider_dashboard')
    #if the user associated with the request is of user_type = patient
    elif request.user.is_patient():
        #redirect them to the patient dashboard
        return redirect('patient_dashboard')
    
    #otherwise redirect the user to the landing page
    return redirect('welcome')



