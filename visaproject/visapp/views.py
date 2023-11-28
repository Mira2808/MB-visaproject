from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import Clientprofile,Document,Inquiry
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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

          inquiry_object=Inquiry(name=name,email=email,phoeno=phoneno,message=message)
          inquiry_object.save()
          return redirect("index")
     return render(request,"client/index.html")    

def registration(request):
     if request.method=="POST":
          username=request.POST.get('username')
          first_name=request.POST.get('fname')
          last_name=request.POST.get('lname')
          email=request.POST.get('email')
          phoneno=request.POST.get('phoneno')
          date_of_birth=request.POST.get('date_of_birth')
          education=request.POST.get('education')
          ielts=request.POST.get('ielts')
          password=request.POST.get('password')
          confirmpassword=request.POST.get('confirmpassword')
     
          # below left side value=models, right side=views

          user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
          profile=Clientprofile(phone=phoneno,date_of_birth=date_of_birth,current_education=education,IELTSAppeared=ielts,user_model=user)
          user.save()
          profile.save()
          return redirect("index")
     context = {"profile": global_user(request)}

     return render(request,"client/regis.html",context=context) 


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        return redirect("index")
    context = {"profile": global_user(request)}
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
     return render(request,"client/contact.html")  


# def ielts(request):
#      return render(request,"client/ielts.html")  

# def singapore(request):
#      return render(request,"client/singapore.html")     

def country(request, country):
     print(country)
     return render(request, f"client/{country}.html")

def coaching1(request, coaching1):
     print(country)
     return render(request, f"coach/{coaching1}.html")





# def editprofile(request,user_id):
     
#      user_detail=User.objects.filter(id=user_id).first()
#      # print(id,user_detail)
#      if request.method == "POST":
#           username=request.POST.get('username')
#           first_name=request.POST.get('first_name')
#           last_name=request.POST.get('last_name')
#           email=request.POST.get('email')
#           phoneno=request.POST.get('phoneno')
#           date_of_birth=request.POST.get('date_of_birth')
#           education=request.POST.get('education')
#           ielts=request.POST.get('ielts')
#           password=request.POST.get('password')
          


#           user=User.objects.filter(id=user_id).first()
#           user=Clientprofile.objects.filter(id=user_detail).first()
#           user.username=username
#           user.first_name=first_name
#           user.last_name=last_name
#           user.email=email
#           user.phoneno=phoneno
#           user.date_of_birth=date_of_birth
#           user.education=education
#           user.ielts=ielts
#           user.password=password
#           user.save()
#           return redirect("index")
#      context = {"profile": global_user(request), "user_detail":user_detail}
#      return render(request,"client/editprofile.html") 

def document(request):
     if request.method == "POST":
          country=request.POST.get("country")
          visatype=request.POST.get("visatype")
          passport=request.FILES.get("passport")
          photo=request.FILES.get("photo")
          passport=request.FILES.get("passport")
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
          return redirect("index")
     return render(request,"client/document.html")  





