from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def patient_dashboard(request):
    #render the patient dashbaord if logged in
    return HttpResponse("Welcome to the patient dashboard!")

