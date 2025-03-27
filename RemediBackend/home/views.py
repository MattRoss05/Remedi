from django.shortcuts import render

# Create your views here.

#Render welcome page
def welcome_page(request):
    return render(request, 'home/welcome.html')
