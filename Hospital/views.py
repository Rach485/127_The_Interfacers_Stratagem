from django.shortcuts import render,redirect
from django.http import HttpResponse 
from app.models import patient

 

def BASE(request):
    return render(request,'base.html')

def ADD_PATIENT(request):
    return render(request,'template\patient\add_patients.html')

def homepage(request):
    return render(request,"home.html")

def add_patients(request):

    '''if request.method == "POST":
      
      patient_name=request.POST.get('patient_name')
      dob=request.POST.get('dob')
      age=request.POST.get('age')
      phone=request.POST.get('phone')
      email=request.POST.get('email')
      gender=request.POST.get('gender')
      address=request.POST.get('address')'''
     
    '''patient=patient(
          patient_name=patient_name,
          Date_of_birth=dob,
          age=age,
          phone=phone,
          email=email,
          gender=gender,
          address=address,
      )'''
      #patient.save()
      #File=
      #print(patient_name,dob,age,phone,email,gender,address)
    return render(request,"adding_patient.html")

def savePatient(request):
    if request.method == "POST":
        patient_name=request.POST.get('patient_name')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        en=patient( patient_name= patient_name,Date_of_birth =dob,age=age,phone=phone,email=email, gender=gender,address=address)
        en.save()
    return render(request,"adding_patient.html")

def about_patient(request):
    return render(request,"about-patient.html")

def patient_details(request):
    return render(request,'patients.html')

def add_appointments(request):
    return render(request,'add-appointment.html')
