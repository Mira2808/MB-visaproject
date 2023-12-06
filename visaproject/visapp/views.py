from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import Clientprofile,Document,Inquiry,Contactus, Adviserprofile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def global_user(request):
    profile = ''
    if request and request.user and request.user.id:
        profile = Clientprofile.objects.filter(user_model=request.user).first()
    return profile

def index(request):
     if request.method=="POST":
          name=request.POST.get("name")
          email=request.POST.get("email")
          phoneno=request.POST.get("phoneno")
          message=request.POST.get("message")

          inquiry_object=Inquiry(name=name,email=email,phoneno=phoneno,message=message)
          inquiry_object.save()
          return redirect("index")
     # print(request.user)
     base_user = User.objects.filter(username=request.user).first()
     client_user = Clientprofile.objects.filter(user_model=base_user.id).first() if base_user else None 
     adviser_user = Adviserprofile.objects.filter(user_model=base_user.id).first() if base_user else None

     if client_user:
          return render(request,"client/index.html")    
     elif adviser_user:
          return render(request,"visadviser/index.html")
     else:
          return render(request,"client/index.html")


def registration(request):
     message =""
     if request.method=="POST":
          csrf_token = request.POST.get('csrfmiddlewaretoken')
          username=request.POST.get('username')
          first_name=request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          email=request.POST.get('email')
          phoneno=int(request.POST.get('phoneno'))
          date_of_birth=request.POST.get('date_of_birth') if request.POST.get('date_of_birth') else datetime.datetime.now()  
          education=request.POST.get('education')
          if request.POST.get('ielts') == 'yes':
               ielts= True 
          else: 
               ielts= False 
          password=request.POST.get('password')
          confirmpassword=request.POST.get('confirmpassword')
     
          # below left side value=models, right side=views
          usern=User.objects.filter(username=username).first()
          usere=User.objects.filter(email=email).first()

          if usern:
               message="username already exists,please enter diffrent username"
          elif usere:
               message="email already exists,please enter diffrent email"
          elif password !=confirmpassword:
               message="password and confirmpassword doesnot matches"
          else:
               user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
               profile=Clientprofile(phone=phoneno,date_of_birth=date_of_birth,current_education=education,IELTSAppeared=ielts,user_model=user)
               user.save()
               profile.save()
               return redirect("index")
     context = {"profile": global_user(request),"message":message}

     return render(request,"client/regis.html",context=context) 


def user_login(request):
    message=""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        else:
             message="invalid username password"
        return redirect("index")
    context = {"profile": global_user(request),"message":message}
    return render(request, 'client/login.html', context=context)

def user_logout(request):
     logout(request)
     return redirect("user_login")

def service(request):
     return render(request,"client/service.html")

def coaching(request):
     return render(request,"client/coaching.html")

def about(request):
     return render(request,"client/about.html")  

def countries(request):
     return render(request,"client/countries.html")  

def contact(request):
     if request.method=="POST":
          fname=request.POST.get("fname")
          lname=request.POST.get("lname")
          email=request.POST.get("email")
          phoneno=request.POST.get("phoneno")
          message=request.POST.get("message")

          contact_object=Contactus(fname=fname,lname=lname,email=email,phoneno=phoneno,message=message)
          contact_object.save()
          return redirect("index")

     return render(request,"client/contact.html")  


def ielts(request):
     return render(request,"client/ielts.html")

def pte(request):
     return render(request,"client/pte.html") 

def gmat(request):
     return render(request,"client/gmat.html")   
   

def country(request, country):
     print(country)
     return render(request, f"client/{country}.html")

@csrf_exempt
def editprofile(request,user_id):
     
     user_detail=User.objects.filter(id=user_id).first()
     # print(id,user_detail)
     if request.method == "POST":
          username=request.POST.get('username')
          first_name=request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          email=request.POST.get('email')
          phoneno=request.POST.get('phoneno')
          date_of_birth=request.POST.get('date_of_birth')
          education=request.POST.get('education')
          if request.POST.get('ielts') == 'yes':
               ielts= True 
          else: 
               ielts= False 
          password=request.POST.get('password')
          


          user=Clientprofile.objects.filter(user_model=user_detail.id).first()
          user_detail.username=username
          user_detail.first_name=first_name
          user_detail.last_name=last_name
          user_detail.email=email
          user.phone=phoneno
          user.date_of_birth=date_of_birth
          user.current_education=education
          user.IELTSAppeared=ielts
          user_detail.set_password = password
          user.save()
          user_detail.save()
          return redirect("index")
     context = {"profile": global_user(request), "user_detail":user_detail}
     return render(request,"client/editprofile.html") 

def document(request):
     message = ""
     if request.method == "POST":
          country=request.POST.get("country")
          visatype=request.POST.get("visatype")
          passport=request.FILES.get("passport")
          photo=request.FILES.get("photo")
          bankstatement=request.FILES.get("bankstatement")
          itr=request.FILES.get("itr")
          hotelconfirm=request.FILES.get("hotelconfirm")
          employeeproof=request.FILES.get("employeeproof")
          jobproof=request.FILES.get("jobproof")
          propertyproof=request.FILES.get("propertyproof")
          investment=request.FILES.get("investment")
          leaveletter=request.FILES.get("leaveletter")
          APD=request.FILES.get("APD")
          accommodation=request.FILES.get("accommodation")
          marriagecerti=request.FILES.get("marriagecerti")
          childrenproof=request.FILES.get("childrenproof")

          if not passport or not photo or not bankstatement or not propertyproof or not APD:
               message = "Please upload the required documents."
          else:
               document_object=Document(country=country,visatype=visatype,
                                        passport=passport,photo=photo,
                                        bankstatement=bankstatement,itr=itr,
                                        hotelconfirm=hotelconfirm,employeeproof=employeeproof,
                                        jobproof=jobproof,propertyproof=propertyproof,
                                        investment=investment,leaveletter=leaveletter,
                                        APD=APD,accommodation=accommodation,
                                        marriagecerti=marriagecerti,childrenproof=childrenproof
                                        )
               document_object.save()
               return redirect("document")
     context = {"message": message}
     return render(request,"client/document.html", context=context)  


def vindex(request):
     return render(request,"visadviser/vindex.html")  


def aindex(request):
     return render(request,"main-admin/aindex.html")  
     


