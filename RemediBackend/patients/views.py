from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def patient_dashboard(request):
    if request.user.is_authenticated:
        #render the patient dashbaord if logged in
        return HttpResponse("Welcome to the patient dashboard!")
    else:
        return redirect('welcome')

