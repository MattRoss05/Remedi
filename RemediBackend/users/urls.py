from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.register_page, name = "register"),
   path('redirect/', views.role_based_redirect, name = 'role_based_redirect'),
]