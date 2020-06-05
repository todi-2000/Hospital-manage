from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
category_choices = ( 
    ("Patient", "Patient"),
    ("Doctor", "Doctor"),
) 

Gender_choices = ( 
    ("Male", "Male"),
    ("Female", "Female"),
) 

Status_choices = ( 
    ("Completed", "Completed"),
    ("Pending", "Pending"),
) 

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=100,blank=True, null=True)
    Lastname=models.CharField(max_length=100,blank=True, null=True)
    Email=models.EmailField(max_length=200)
    Phone=models.CharField(max_length=10)
    Registeras=models.CharField(max_length=30,blank=True, null=True,choices=category_choices)
    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100,default=None)
    Age=models.IntegerField(default=0)
    Gender=models.CharField(max_length=20,choices=Gender_choices,default=None)
    Address=models.CharField(max_length=500,default=None)
    Outstanding=models.CharField(max_length=50,default=0)
    Paid=models.CharField(max_length=50,default=0)
    BloodType=models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.Name

class Doctor(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100,default=None)
    Age=models.IntegerField(default=0)
    Gender=models.CharField(max_length=20,choices=Gender_choices,default=None)
    Address=models.CharField(max_length=500,default=None)
    BloodType=models.CharField(max_length=50,default=None)
    Department=models.CharField(max_length=20,default=None)
    Salary=models.IntegerField(default=0)
    Attendance=models.IntegerField(default=0)
    def __str__(self):
        return self.Name

class Appointment(models.Model):
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=  models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=Status_choices,default=None)

    def __str__(self):
        return self.date

class Prescription(models.Model):
    Docname=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    prescription=models.TextField(max_length=200)
    Disease=models.TextField(max_length=50)
    Patname=models.ForeignKey(Patient,on_delete=models.CASCADE)
    

class Reception(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class HR(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)