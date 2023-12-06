from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Document)
admin.site.register(models.Clientprofile)
admin.site.register(models.Service)
admin.site.register(models.Adviserprofile)
admin.site.register(models.Inquiry)
admin.site.register(models.Country)
admin.site.register(models.Payment)  
admin.site.register(models.Contactus)
   