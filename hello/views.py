from django.shortcuts import render, redirect
from django.utils.timezone import datetime
# Create your views here.
from django.http import HttpResponse
from .models import Report,File,Appointment,Client,Vet,Log_in
from django.db.models import Max
def home(request):
    return render(request, "hello/home.html")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")
def login(request):
    return render(request, "hello/")

def menuUser(request):
    return render(request,"menu-bootstrap/a/menuUser.html")

def menuVet(request):
    return render(request,"menu-bootstrap/a/menuVet.html")

def login(request):
    return render(request, "hello/login.html")


def appointment(request):
    return render(request, "hello/appointment.html")

def backtest(request, appointment):
    searchAppointment = int(appointment)
    checkupdate= request.GET.get('checkUpdate')
    files = None
    vet = None
    appointment = None
    pet = None
    report = None
    priority=None
    if searchAppointment:
        report = Report.objects.filter(appointement_id=searchAppointment).order_by('-report_id')[0]
        files = File.objects.filter(report_id=report.report_id)
        vet = report.appointement_id.vet_id
        appointment = report.appointement_id
        pet = appointment.pet_id
    elif checkupdate and searchAppointment:
        report = Report.objects.filter(appointement_id=searchAppointment).order_by('-report_id')[0]
        files = File.objects.filter(report_id=report.report_id)
        vet = report.appointement_id.vet_id
        appointment = report.appointement_id
        pet = appointment.pet_id
        report2= Report(report.report_id,appointment.appointment_id,report.medical_history_id,request.Get.get('test'),report.diagnosis,report.prescribed_treatment, report.recommendations,report.additional_note,report.update_note)
        report2.save()
    else:
        report=None
        vet=None
    return render(request, 'hello/appointment.html', {
        'searchAppointment': searchAppointment,
        'report': report,
        'files': files,
        'vet': vet,
        'appointment': appointment,
        'pet': pet,
        'checkUpdate':checkupdate,
    })
def registerPet(request):
    return render(request,'hello/registerPet.html')
def appointmentCreate(request):
    return render(request,'hello/appointmentCreate.html')
def appointmentView(request):
    return render(request, 'hello/appointmentView.html')
def rateVet(request):
    return render(request, 'hello/rateVet.html')
def registerPet(request):
    return render(request, 'hello/registerPet.html')
def viewPets(request):
    return render(request,'hello/viewPets.html')
def viewVets(request):
    return render(request, 'hello/viewVets.html')