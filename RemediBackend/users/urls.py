#import path function from django.urls to provide views to certain urls
from django.urls import path
#import views of the users application
from . import views

urlpatterns = [
    #if the path contains register, call the register_page view
    # and name it 'register" to be called on in our hyperlinks
    #in the html templates
   path('register/', views.register_page, name = "register"),
   #if path contains redirect, call role_based_redirect
   #name it the same as the view to be later called on in the
   #hyperlinks of our html templates
   path('redirect/', views.role_based_redirect, name = 'role_based_redirect'),
]