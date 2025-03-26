from django.shortcuts import render, redirect
from .forms import ProviderRegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_page(response):
    if response.method == "POST":
        form = ProviderRegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = ProviderRegisterForm()
    return render(response, 'users/register.html', {"form": form})

@login_required
def role_based_redirect(request):
    if request.user.is_provider():
        return redirect('provider_dashboard')
    elif request.user.is_patient():
        return redirect('patient_dashboard')
    return redirect('welcome')



