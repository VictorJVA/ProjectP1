from django.shortcuts import render
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in,Pets


def backtest(request, appointment):
    searchAppointment = appointment
    searchAppointment2=Appointment.objects.filter(appointment_id=appointment)
    checkupdate= request.GET.get('checkUpdate')
    files = None
    vet = None
    appointment = None
    pet = None
    report = None
    priority=None
    if searchAppointment2 and not checkupdate:
        report = Report.objects.filter(appointement_id=searchAppointment).order_by('-report_id')[0]
        files = File.objects.filter(report_id=report.report_id)
        vet = report.appointement_id.vet_id
        appointment = report.appointement_id
        pet = appointment.pet_id
    elif checkupdate and searchAppointment2:
        report = Report.objects.filter(appointement_id=searchAppointment).order_by('-report_id')[0]
        files = File.objects.filter(report_id=report.report_id)
        vet = report.appointement_id.vet_id
        appointment = report.appointement_id
        pet = appointment.pet_id
        report2= Report(report.report_id+1,appointment.appointment_id,report.medical_history_id.Medical_history_id,request.GET.get('test'),request.GET.get('diagnosis'),request.GET.get('prescribed_treatment'),request.GET.get('aditional_recomend'),request.GET.get('aditional_notes'),request.GET.get('checkUpdate'))
        report2.save()
        report=report2
    else:
        report=None
        vet=None
    return render(request, 'appointment.html', {
        'searchAppointment': searchAppointment,
        'report': report,
        'files': files,
        'vet': vet,
        'appointment': appointment,
        'pet': pet,
        'checkUpdate':checkupdate,
    })

def viewPets(request):
    return render(request,'viewPets.html')

def save(request):    
    return render(request, 'save.html')

def appointmentOutside(request, user_id):
    appointment = list(Appointment.objects.filter(vet_id=user_id).order_by('pet_id').values_list('pet_id').distinct())
    print(appointment)

    client = Client.objects.all()

    return render(request, 'appointmentsOutside.html', {'user': appointment})


def appointmentInside(request, user_id):

    appointment = Appointment.objects.filter(vet_id=user_id)
    
    client = Vet.objects.get(vet_id=user_id)

    return render(request, 'appointmentInside.html', {'appointment': appointment,'client':client})


def clinicalUserView(request, user_id, pet_id):
    pets=None
    client=Vet.objects.get(vet_id=user_id)
    if(Appointment.objects.filter(vet_id=user_id)!=None):
        pets = Pets.objects.get(pet_id=pet_id) 

    return render(request, 'clinicalUserView.html', {'pets': pets,'client':client})