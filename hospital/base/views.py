from django.shortcuts import render,redirect
from .forms import UserForm,ProfileForm,PrescriptionForm,AppointmentForm,PatientForm,DoctorForm,ProfileForm1
from .models import Profile,Patient,Doctor,Appointment,Prescription,Reception,HR
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'base/home.html')

@login_required
def rhome(request):
    return render(request,'reception/home.html')

@login_required
def phome(request):
    return render(request,'patient/home.html')

@login_required
def dhome(request):
    return render(request,'doctor/home.html')

@login_required
def hhome(request):
    return render(request,'hr/home.html')

def contact(request):
    return render(request,'base/contact.html')

def register(request):
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
            elif Profile.objects.get(user=user1).Registeras=="Patient":
                return redirect('phome')
            elif Profile.objects.get(user=user1).Registeras=="Doctor":
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
        if patient.Registeras=="Patient":
            id=Patient.objects.get(user=patient).id
            app=Appointment.objects.filter(Patient_id=id)
            return render(request,'patient/appointment.html',{'app':app})
        elif patient.Registeras=="Doctor":
            id=Doctor.objects.get(user=patient).id
            app=Appointment.objects.filter(Patient_id=id)
            return render(request,'doctor/appointment.html',{'app':app})
    else:
        return redirect('login')

def prescription(request):
    if request.user.is_authenticated:
        name=request.user.username
        profile=User.objects.get(username=name)
        patient=Profile.objects.get(user=profile)
        if patient.Registeras=="Patient":
            id=Patient.objects.get(user=patient).id
            pre=Prescription.objects.filter(Patname_id=id)
            return render(request,'patient/mh.html',{'pre':pre})
        elif patient.Registeras=="Doctor":
            id=Doctor.objects.get(user=patient).id
            pre=Prescription.objects.filter(Patname_id=id)
            return render(request,'doctor/prescription.html',{'pre':pre})
    else:
         return redirect('login')

def pre_new(request):
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

@login_required
def dashboard(request):
    app=Appointment.objects.all()
    pat=Patient.objects.all()
    context={
        'app':app,
        'pat':pat,
    }
    return render(request,'reception/dashboard.html',context)

def createapp(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('dash')
    else:
        form = AppointmentForm()
    return render(request, 'reception/createapp.html', {'form': form})

def createpat(request):
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

def ddashboard(request):
    doc=Doctor.objects.all()
    context={
        'doc':doc,
    }
    return render(request,'hr/dashboard.html',context)


def createdoc(request):
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