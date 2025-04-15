"""
URL configuration for RemediBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as userviews

urlpatterns = [
    #add admin site to available urls
    path('admin/', admin.site.urls),
    #add the urls for the landing page
    path('', include('home.urls')),
    #add urls for register and redirection
    path('user/', include('users.urls')),
    #include this so we can use django, built in login authentication
    path('', include('django.contrib.auth.urls')),
    #allows for us to access patient dashboard
    path('patients/', include('patients.urls')),
    #allows for us to access patient dashboard
    path('providers/', include('providers.urls')),
    #allows for use to logout, called in the provider dashboard
    #html file
    path('log-out/', auth_views.LogoutView.as_view(next_page = 'welcome'), name = 'logout'),
]
