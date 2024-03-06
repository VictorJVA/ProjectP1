from django.shortcuts import render
from hello.models import Report,File,Appointment,Client,Vet,Log_in


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
        report = Report.objects.filter(appointement_id=searchAppointment).order_by('-date_created')[0]
        files = File.objects.filter(report_id=report.report_id)
        vet = report.appointement_id.vet_id
        appointment = report.appointement_id
        pet = appointment.pet_id
    elif checkupdate and searchAppointment2:
        report = Report.objects.filter(appointement_id=searchAppointment).order_by('date_created')[0]
        reportid= Report.objects.filter(appointement_id=searchAppointment).order_by('-report_id')[0]
        files = File.objects.filter(report_id=report.report_id)
        vet = report.appointement_id.vet_id
        appointment = report.appointement_id
        pet = appointment.pet_id
        report2= Report(reportid.report_id+1,appointment.appointment_id,report.medical_history_id.Medical_history_id,request.GET.get('test'),request.GET.get('diagnosis'),request.GET.get('prescribed_treatment'),request.GET.get('aditional_recomend'),request.GET.get('aditional_notes'),request.GET.get('checkUpdate'))
        report2.save()
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