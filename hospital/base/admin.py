from django.contrib import admin
from .models import Profile,Patient,Doctor,Appointment,Prescription,Reception,HR,Accounts

# Register your models here.
admin.site.register(Profile)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Reception)
admin.site.register(HR)
admin.site.register(Accounts)