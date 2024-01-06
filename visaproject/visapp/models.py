from django.db import models
from django.contrib.auth.models import User

# Create your models here.

COUNTRY=[
    ("australia","australia"),
    ("canada","canada"),
    ("europe","europe"),
    ("newzeland","newzeland"),
    ("singapore","singapore"),
]
VISATYPE=[
    ("business","business"),
    ("work","work"),
    ("tourist","tourist"),
    ("student","student"),
]

class Document(models.Model):
    country=models.CharField(max_length=20,choices=COUNTRY)
    visatype=models.CharField(max_length=20,choices=VISATYPE)
    passport=models.FileField(blank=False, null=False)
    photo=models.FileField(blank=False, null=False)
    bankstatement=models.FileField(blank=False, null=False)
    itr=models.FileField(blank=True, null=True)
    hotelconfirm=models.FileField(blank=True, null=True)
    employeeproof=models.FileField(blank=True, null=True)
    jobproof=models.FileField(blank=True, null=True)
    propertyproof=models.FileField(blank=False, null=False)
    investment=models.FileField(blank=True, null=True)
    leaveletter=models.FileField(blank=True, null=True)
    APD=models.FileField(blank=False, null=False)
    accommodation=models.FileField(blank=True, null=True)
    marriagecerti=models.FileField(blank=True, null=True)
    childrenproof=models.FileField(blank=True, null=True)
    user_model = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Document"  


EDUCATION=[
    ("below 12","below 12"),
    ("12","12"),
    ("diploma","diploma"),
    ("graduate","graduate"),
    ("masters","masters"),

]
class Clientprofile(models.Model):
    phone = models.BigIntegerField()
    date_of_birth = models.DateField(blank=True, null=True)
    current_education = models.CharField(max_length=20,choices= EDUCATION, blank=True, null=True)
    IELTSAppeared=models.BooleanField(blank=True, null=True)
    user_model = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __int__(self):
        return self.phone
    
    class Meta:
        verbose_name_plural = "clientprofile"



class Service(models.Model):
    service_name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.service_name
    
    class Meta:
        verbose_name_plural = "service"


class Adviserprofile(models.Model):

    """if new flieds need to be added extend null=true and blanl=true"""
    phone = models.BigIntegerField()
    date_of_birth = models.DateField()
    experience=models.FloatField()
    qualification=models.CharField(max_length=50)
    email=models.EmailField()
    location=models.CharField(max_length=50)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    user_model = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Adviserprofile"


class Inquiry(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    phoneno=models.BigIntegerField(blank=True,null=True)
    message=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "inquiry"

class Contactus(models.Model):
    fname=models.CharField(max_length=50,blank=True,null=True)
    lname=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    phoneno=models.BigIntegerField(blank=True,null=True)
    message=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.fname
    
    class Meta:
        verbose_name_plural = "Contactus"


class Country(models.Model):
    country_name=models.CharField(max_length=128)
    image=models.ImageField()
    description=models.TextField()

    def __str__(self):
        return self.country_name
    
    class Meta:
        verbose_name_plural = "country"


class Payment(models.Model):
    order_no=models.CharField(max_length=50)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    amount=models.BigIntegerField()
    status=models.CharField(max_length=50)
    user_model = models.ForeignKey(User, on_delete=models.CASCADE)
    Adviserprofile=models,models.ForeignKey(Adviserprofile,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "payment"
    








