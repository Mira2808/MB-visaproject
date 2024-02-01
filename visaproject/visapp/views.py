from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import Clientprofile,Document,Inquiry,Contactus, Adviserprofile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import razorpay


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
          return render(request,"visadviser/vindex.html")
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
     user=Clientprofile.objects.filter(user_model=user_detail.id).first()
     dateofbirth=user.date_of_birth.strftime("%Y-%m-%d")
     # print(dateofbirth,type(dateofbirth))
     if request.method == "POST":
          username=request.POST.get('username')
          first_name=request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          email=request.POST.get('email')
          phoneno=request.POST.get('phoneno')
          date_of_birth=request.POST.get('date_of_birth')
          print(type(date_of_birth),date_of_birth)
          education=request.POST.get('education')
          IELTS=request.POST.get('ielts')
          password=request.POST.get('password')
          


          
          user_detail.username=username
          user_detail.first_name=first_name
          user_detail.last_name=last_name
          user_detail.email=email
          user.phone=phoneno
          user.date_of_birth=date_of_birth
          user.current_education=education
          user.IELTSAppeared=IELTS
          user_detail.set_password = password
          user.save()
          user_detail.save()
          return redirect("index")
     context = {"profile": global_user(request), "user_detail":user_detail,
                "user":user,"dateofbirth":dateofbirth}
     return render(request,"client/editprofile.html",context=context) 

@csrf_exempt
def editpassword(request,user_id):
       message=""
       user_detail=User.objects.filter(id=user_id).first()
       if request.method == "POST":
            old_password=request.POST.get('old_password')
            new_password=request.POST.get('new_password')
            repeat_password=request.POST.get('repeat_password')
            return redirect("index")
       if user_detail.check_password(old_password):
            if new_password==repeat_password:
                 user_detail.password=new_password
                 user_detail.save()
            else:
               message="your new_password and repeate password does not match"
            
     
               context={"profile": global_user(request),"user_detail":user_detail,"message":message}

       return render(request,"client/editpassword.html",context=context) 


def create_payment(visatype):
     if visatype == "asdjahsd":
          amount = 21334
     else:
          pass
     client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
     data = {
     'amount': amount,
     'currency': 'INR',
     'receipt': 'order_rcptid_11',
     'payment_capture': 1  # Auto-capture the payment
     }
     order = client.order.create(data=data)
     print(order)
     return order


def document(request):
     user=User.objects.all()
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

          order_no = create_payment(visatype)
          if not order_no:
               message = "Payment unsuccessful, please retry again!"
               return
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

def registeruser(request,user_id):
     registeruser=User.objects.all() 
     # registeruser2=Clientprofile.objects.filter(id=user_id).first()
     registeruser2=Clientprofile.objects.all()
     context={"registeruser":registeruser,"registeruser2":registeruser2,"profile": global_user(request)}
     return render(request,"visadviser/registeruser.html",context=context)  

def v_editprofile(request):
     return render(request,"visadviser/v_editprofile.html")

def inquiry(request):
     inquiry_details=Inquiry.objects.all()
     context={"inquiry_details":inquiry_details}
     return render(request,"visadviser/inquiry.html",context=context)


def v_contact(request):
     contact_details=Contactus.objects.all()
     context={"contact_details":contact_details}
     return render(request,"visadviser/v_contact.html",context=context)

def v_document(request, user_id):
     document_detail=Document.objects.filter(user_model_id=user_id).all()
     print(len(document_detail))
     context={"document_detail":document_detail,"profile": global_user(request)}
     return render(request,"visadviser/v_document.html",context=context)

def editregisteruser(request,user_id):
     registeruser=User.objects.filter(id=user_id).first()
     registeruser2=Clientprofile.objects.filter(id=user_id).first()
     context={"registeruser":registeruser,"registeruser2":registeruser2,"profile": global_user(request)}
   
     return render(request,"visadviser/editregisteruser.html",context=context)

def del_inq(request,inq_id):
     inq_obj=Inquiry.objects.filter(id=inq_id).first()
     if request.method == "POST": 
          inq_obj.delete()
          return redirect("int_obj")
     context={"inq_obj":inq_obj}
     return render(request,"visadviser/del_inq.html",context=context)

def del_con(request,c_id):
     con_obj=Contactus.objects.filter(id=c_id).first()
     if request.method == "POST":
          con_obj.delete()
          return redirect("del_con")
     context={"con_obj":con_obj}
     return render(request,"visaadviser/del_con.html",context=context)




def aindex(request):
     return render(request,"main-admin/aindex.html")  
     


