
from django.urls import path
from . import views

urlpatterns = [
   path('index/',views.index,name='index'),
   path('registration/',views.registration,name='registration'),
   path('service/',views.service,name='service'),
   path('coaching/',views.coaching,name='coaching'),     
   path('about/',views.about,name='about'), 
   path('countries/',views.countries,name='countries'),
   path('contact/',views.contact,name='contact'),
   path('login/',views.login,name='login'),
   path('ilets/',views.ilets,name='ilets'),
   path('singapore/',views.singapore,name='singapore'),
   
   
   
]