
from django.contrib import admin
from django.urls import path
from Hospital import views

#from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.BASE,name='base'),

    path('patient/add',views.ADD_PATIENT,name='add_patients.html'),
    path('',views.homepage),
    path('add_patients',views.add_patients,name='adding_patient.html'),
    path('savepatient',views.savePatient,name='savepatient'),
    path('about-patient',views.about_patient,name='about-patient.html'),
    path('adding_patients',views.add_patients,name='adding_patients.html'),
    path('patient_details',views.patient_details,name='patients.html'),
    path('add_appointments',views.add_appointments,name='add-appointment.html'),
]
