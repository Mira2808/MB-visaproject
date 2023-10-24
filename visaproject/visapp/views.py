from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
     return render(request,"index.html")    

def registration(request):
     return render(request,"regis.html")       