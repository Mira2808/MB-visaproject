
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
   path('user_login/',views.user_login,name='user_login'),
   path('user_logout/',views.user_logout,name='user_logout'),
   path('ielts/',views.ielts,name='ielts'),
   path('pte/',views.pte,name='pte'),
   path('gmat/',views.gmat,name='gmat'),
   path('client/<str:country>/', views.country, name="client"),
   path('editprofile/<str:user_id>/', views.editprofile, name="editprofile"),
   path('document/', views.document, name="document"),

   path('visadviser/vindex',views.vindex,name="vindex"),
   path('visadviser/registeruser',views.registeruser,name="registeruser"),
   path('visadviser/editprofile',views.editprofile,name="editprofile"),


   path('main-admin/aindex',views.aindex,name="aindex"), 
   
   
]