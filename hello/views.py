from django.shortcuts import render
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

def backtest(request):
    searchAppointment = request.GET.get('searchAppointment')
    searchVet = None
    files = None
    vet = None
    appointment = None
    pet = None
    report = None
    
    if request.method == 'GET' and searchAppointment:
        try:
            report = Report.objects.get(appointement_id=searchAppointment)
        except Report.DoesNotExist:
            # If no report exists, generate a report ID
            report_id = Report.objects.aggregate(max_report_id=Max('report_id'))['max_report_id']
            report_id = report_id + 1 if report_id is not None else 1
            report = Report.objects.create(report_id=report_id, appointement_id=searchAppointment)
            #report.save()
        
        # Fetch additional details
        searchVet = request.GET.get('searchVet')
        files = File.objects.filter(report_id=report.report_id)
        vet = report.appointement_id.vet_id
        appointment = report.appointement_id
        pet = appointment.pet_id
    
    elif request.method == 'GET':
        max_appointment_id = Appointment.objects.aggregate(max_appointment_id=Max('appointment_id'))['max_appointment_id']
        max_appointment_id = max_appointment_id + 1 if max_appointment_id is not None else 1
        appointment = Appointment(appointment_id=max_appointment_id)
        #appointment.save()
        
    return render(request, 'hello/appointment.html', {
        'searchAppointment': searchAppointment,
        'searchVet': searchVet,
        'report': report,
        'files': files,
        'vet': vet,
        'appointment': appointment,
        'pet': pet
    })
