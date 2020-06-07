from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate, get_user_model
from .models import Profile,Prescription,Appointment,Patient,Doctor,Accounts

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["Firstname","Lastname","Email","Phone","Registeras"]

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model=Prescription
        fields=["Patname","Disease","prescription"]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields=["Patient","Doctor","date","time","status"]

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"
        exclude=["user","Paid","Outstanding"]

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"
        exclude=["user"]

class ProfileForm1(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["Email","Phone"]

class AccountForm(forms.ModelForm):
    class Meta:
        model=Accounts
        fields="__all__"
        exclude=["user"]