from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
     return render(request,"client/index.html")    

def registration(request):
     return render(request,"client/regis.html") 

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

def login(request):
     return render(request,"client/login.html") 

def ilets(request):
     return render(request,"client/ilets.html")

def singapore(request):
     return render(request,"client/singapore.html")

 


   
