from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class document(models.Model):
    marksheet=models.FileField()
    
    class Meta:
        verbose_name_plural = "document"


EDUCATION=[
    ("below 12","below 12"),
    ("12","12"),
    ("diploma","diploma"),
    ("graduate","graduate"),
    ("masters","masters"),

]
class Clientprofile(models.Model):
    phone = models.BigIntegerField()
    date_of_birth = models.DateField()
    current_education = models.CharField(max_length=20,choices= EDUCATION)
    IELTSAppeared=models.BooleanField()
    user_model = models.ForeignKey(User, on_delete=models.CASCADE)
    documnent=models.ForeignKey(document,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_model
    
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
        return self.user_model
    
    class Meta:
        verbose_name_plural = "Adviserprofile"


class Inquirey(models.Model):
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    message=models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "inquirey"


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
    








