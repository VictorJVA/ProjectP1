from django.shortcuts import render
from .models import Report,File,Appointment,Client,Vet,Log_in


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
