from django.shortcuts import render,redirect
from .forms import UserForm,ProfileForm,PrescriptionForm,AppointmentForm,PatientForm,DoctorForm,ProfileForm1
from .models import Profile,Patient,Doctor,Appointment,Prescription,Reception,HR
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user1=User.objects.get(username=request.user.username)
        if Reception.objects.filter(user=user1).exists():
            return redirect('rhome')
        elif HR.objects.filter(user=user1).exists():
            return redirect('hhome')
        elif Patient.objects.filter(user=Profile.objects.get(user=user1)).exists():
            return redirect('phome')
        elif Doctor.objects.filter(user=Profile.objects.get(user=user1)).exists():
            return redirect('dhome')
    return render(request,'base/home.html')

@login_required(login_url='/login/')
def rhome(request):
    return render(request,'reception/home.html')

@login_required(login_url='/login/')
def phome(request):
    return render(request,'patient/home.html')

@login_required(login_url='/login/')
def dhome(request):
    return render(request,'doctor/home.html')

@login_required(login_url='/login/')
def hhome(request):
    return render(request,'hr/home.html')

def contact(request):
    return render(request,'base/contact.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('logout')
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            if p_form.Registeras=="Doctor":
                d=Doctor(user=p_form)
                d.save()
            if p_form.Registeras=="Patient":
                p=Patient(user=p_form)
                p.save()
            return redirect('login')
    else:
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'base/register.html', {'u_form': u_form, 'p_form': p_form})

def login(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            user1=User.objects.get(username=username)
            if Reception.objects.filter(user=user1).exists():
                return redirect('rhome')
            elif HR.objects.filter(user=user1).exists():
                return redirect('hhome')
            elif Patient.objects.filter(user=Profile.objects.get(user=user1)).exists():
                return redirect('phome')
            elif Doctor.objects.filter(user=Profile.objects.get(user=user1)).exists():
                return redirect('dhome')
        else:
            return redirect('login')
    else:
        return render(request,'base/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def appointment(request):
    if request.user.is_authenticated:
        name=request.user.username
        profile=User.objects.get(username=name)
        patient=Profile.objects.get(user=profile)
        if Patient.objects.filter(user=patient).exists():
            id=Patient.objects.get(user=patient).id
            app=Appointment.objects.filter(Patient_id=id)
            return render(request,'patient/appointment.html',{'app':app})
        elif Doctor.objects.filter(user=patient).exists():
            id=Doctor.objects.get(user=patient).id
            app=Appointment.objects.filter(Doctor_id=id)
            return render(request,'doctor/appointment.html',{'app':app})
    else:
        return redirect('login')

def prescription(request):
    if request.user.is_authenticated:
        name=request.user.username
        profile=User.objects.get(username=name)
        patient=Profile.objects.get(user=profile)
        if Patient.objects.filter(user=patient).exists():
            id=Patient.objects.get(user=patient).id
            pre=Prescription.objects.filter(Patname_id=id)
            return render(request,'patient/mh.html',{'pre':pre})
        elif Doctor.objects.filter(user=patient).exists():
            name=Doctor.objects.get(user=patient)
            pre=Prescription.objects.filter(Docname=name)
            return render(request,'doctor/prescription.html',{'pre':pre})
    else:
         return redirect('login')

@login_required(login_url='/login/')
def pre_new(request):
    if request.user.is_authenticated:
        profile=Profile.objects.get(user=request.user)
        if Doctor.objects.get(user=profile).exists():
            if request.method == "POST":
                form = PrescriptionForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.Docname = request.user
                    post.save()
                    return redirect('pre')
            else:
                form = PrescriptionForm()
            return render(request, 'doctor/form_edit.html', {'form': form})
        else:
            return redirect('login')

@login_required(login_url='/login/')
def dashboard(request):
    app=Appointment.objects.all()
    pat=Patient.objects.all()
    context={
        'app':app,
        'pat':pat,
    }
    return render(request,'reception/dashboard.html',context)

def createapp(request):
    if request.user.is_authenticated:
        if Reception.objects.get(user=request.user).exists():
            if request.method == "POST":
                form = AppointmentForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.save()
                    return redirect('dash')
            else:
                form = AppointmentForm()
            return render(request, 'reception/createapp.html', {'form': form})
        else:
            return redirect('logout')
    else:
        return redirect('login')

@login_required(login_url='/login/')
def createpat(request):
    if request.user.is_authenticated:
        if Reception.objects.get(user=request.user).exists():
            if request.method == "POST":
                u_form=UserForm(request.POST)
                p_form=ProfileForm1(request.POST)
                form = PatientForm(request.POST)
                if form.is_valid() and u_form.is_valid() and p_form.is_valid():
                    p=u_form.save(commit=False)
                    username=p.username
                    p.save()
                    profile=p_form.save(commit=False)
                    profile.user=User.objects.get(username=username)
                    profile.save()
                    post = form.save(commit=False)
                    post.user=Profile.objects.get(user=p)
                    post.save()
                    return redirect('dash')
            u_form=UserForm()
            p_form=ProfileForm1()
            form = PatientForm()
            context={
                'form':form,
                'u_form':u_form,
                'p_form':p_form
            }
            return render(request, 'reception/createpat.html',context)
        else:
            return redirect('login')

@login_required(login_url='/login/')
def ddashboard(request):
    doc=Doctor.objects.all()
    context={
        'doc':doc,
    }
    return render(request,'hr/dashboard.html',context)

@login_required(login_url='/login/')
def createdoc(request):
    if request.user.is_authenticated:
        if HR.objects.get(user=request.user).exists():
            if request.method == "POST":
                u_form=UserForm(request.POST)
                p_form=ProfileForm1(request.POST)
                form = DoctorForm(request.POST)
                if form.is_valid() and u_form.is_valid() and p_form.is_valid():
                    p=u_form.save(commit=False)
                    username=p.username
                    p.save()
                    profile=p_form.save(commit=False)
                    profile.user=User.objects.get(username=username)
                    profile.save()
                    post = form.save(commit=False)
                    post.user=Profile.objects.get(user=p)
                    post.save()
                    return redirect('ddash')
            u_form=UserForm()
            p_form=ProfileForm1()
            form = DoctorForm()
            context={
                'form':form,
                'u_form':u_form,
                'p_form':p_form
            }
            return render(request, 'hr/createdoc.html',context)
        else:
            return redirect('login')
