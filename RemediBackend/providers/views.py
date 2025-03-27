from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def provider_dashboard(request):
    #render the provider dashboard, can only be accessed if logged in
    return render(request, 'providers/providerdashboard.html')