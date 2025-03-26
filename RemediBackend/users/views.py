from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register_page(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, 'users/register.html', {"form": form})

def login_page(request):
    return render(request, 'users/login.html')



