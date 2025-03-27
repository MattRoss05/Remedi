from django.urls import path
from . import views

#allow empty urls to route to the landing page
urlpatterns = [
    #call provide welcome_page and name the url 'welcome' to be
    #referenced in the html templates of our application
    path('', views.welcome_page, name = 'welcome')
]