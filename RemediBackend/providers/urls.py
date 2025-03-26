from django.urls import path
from . import views

urlpatterns = [
    path('', views.provider_dashboard, name = 'provider_dashboard')
]