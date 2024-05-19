from django.shortcuts import render
import json, pdb
from django.http import JsonResponse
from .forms import AppointmentActionForm,AppointmentForm
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
    appointment = list(Appointment.objects.filter(vet_id=user_id).values_list('pet_id',flat=True).order_by('pet_id').distinct())
    newlist=[]
    for i in appointment:
        newlist.append(Pets.objects.get(pk=i).client_id)



    return render(request, 'appointmentsOutside.html', {'user': newlist,'client':Vet.objects.get(pk=user_id)})


def appointmentInside(request, user_id):

    appointment = Appointment.objects.filter(vet_id=user_id)
    
    client = Vet.objects.get(vet_id=user_id)

    return render(request, 'appointmentInside.html', {'appointment': appointment,'client':client})


def clinicalUserView(request, user_id, pet_id):
    pet=None
    client=Vet.objects.get(vet_id=user_id)
    
    if(Appointment.objects.filter(vet_id=user_id).filter(appointment_accepted=True)!=None):
        pet = Pets.objects.filter(pet_id=pet_id) 

    return render(request, 'clinicalUserView.html', {'pets': pet,'client':client})

def appointmentAccept(request, user_id, appointment_id):
    # if request.method == 'POST':
    #     form = AppointmentActionForm(request.POST)
    #     if form.is_valid():
    #         appointment_id = form.cleaned_data['appointment_id']
    #         action = form.cleaned_data['action']
    #         # Perform the action based on the selected choice
    #         if action == 'accept':
    #             appointment = Appointment.objects.get(pk=appointment_id)
    #             appointment.appointment_accepted = True
    #             appointment.save()
    #         elif action == 'reject':
    #             appointment = Appointment.objects.get(pk=appointment_id)
    #             appointment.appointment_accepted = False
    #             appointment.save()
    # else:
    #     form = AppointmentActionForm()
    
    if(isinstance(appointment_id, int)):
        Appointment.objects.filter(pk=appointment_id).update(appointment_accepted=True)
    client=Vet.objects.get(vet_id=user_id)
    appointment= Appointment.objects.filter(vet_id=user_id).filter(appointment_accepted=False)
    return render(request,'appointmentAccept.html',{'client':client,'appointment':appointment})

def createAppointment(request, id_cliente):
    client = Vet.objects.get(pk=id_cliente)
    
    if request.method == 'POST':
        form = AppointmentForm(client_id=id_cliente, data=request.POST)
        if form.is_valid():
            form.save()
            # Aquí podrías agregar un mensaje de éxito o realizar cualquier otra acción necesaria
            form = AppointmentForm(client_id=id_cliente)  # Vaciar el formulario después de enviar los datos exitosamente
    else:
        form = AppointmentForm(client_id= id_cliente)

    context = {
        'form': form,
        'client':client,
    }    

    return render(request, 'vetcreateAppointment.html', context)

def update_field(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        value_to_update = data.get('value')

        # Assuming you have a model named YourModel with a field named 'field_to_update'
        # Retrieve the instance of the model you want to update
        Appointment.objects.filter(pk=value_to_update).update(appointment_accepted=True)  # Adjust this according to your model
        # Return a JSON response indicating success
        return JsonResponse({'success': True})
    else:
        # Return a JSON response indicating failure if the request method is not POST
        return JsonResponse({'success': False, 'error': 'Invalid request method'})