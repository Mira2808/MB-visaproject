from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.document)
admin.site.register(models.Clientprofile)
admin.site.register(models.Service)
admin.site.register(models.Adviserprofile)
admin.site.register(models.Inquirey)
admin.site.register(models.Country)
admin.site.register(models.Payment)