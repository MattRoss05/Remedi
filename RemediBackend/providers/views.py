from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def provider_dashboard(request):
    if request.user.is_authenticated:
        #render the provider dashboard, can only be accessed if logged in
        return render(request, 'providers/providerdashboard.html')
    else:
        return redirect('welcome')