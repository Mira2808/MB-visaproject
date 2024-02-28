
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
   path('editpassword/<str:user_id>/', views.editpassword, name="editpassword"),
   path('document/', views.document, name="document"),

   path('visadviser/vindex',views.vindex,name="vindex"),
   path('visadviser/registeruser',views.registeruser,name="registeruser"),
   path('visadviser/v_editprofile/<str:v_id>/',views.v_editprofile,name="v_editprofile"),
   path('visadviser/inquiry',views.inquiry,name="inquiry"),
   path('visadviser/v_contact',views.v_contact,name="v_contact"),
   path('visadviser/v_document/<str:user_id>/',views.v_document,name="v_document"),
   path('visadviser/editregisteruser/<str:user_id>/',views.editregisteruser,name="editregisteruser"),
   path('visadviser/del_inq/<str:inq_id>/',views.del_inq,name="del_inq"),
   path('visadviser/del_con/<str:c_id>/',views.del_con,name="del_con"),

   path('main-admin/aindex',views.aindex,name="aindex"),
   path('main-admin/v_allocation',views.v_allocation,name="v_allocation"),  
   path('main-admin/a_registeruser',views.a_registeruser,name="a_registeruser"), 
   path('main-admin/edituser/<str:user_id>/',views.edituser,name="edituser"),
   path('main-admin/a_inquiry',views.a_inquiry,name="a_inquiry"), 
   path('main-admin/a_contact',views.a_contact,name="a_contact"), 
   path('main-admin/a_del_inq/<str:inq_id>/',views.a_del_inq,name="a_del_inq"),
   path('main-admin/a_del_con/<str:c_id>/',views.a_del_con,name="a_del_con"),
   
]