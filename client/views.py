from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in, Pets
from django.shortcuts import render, redirect
from .forms import *
import pdb
from datetime import datetime

def homeClient(request, id_cliente):

    client = Client.objects.get(pk=id_cliente)
    pets = Pets.objects.filter(client_id=client)
    # print(pets)
    # pdb.set_trace()
    return render(request, 'homeClient.html', {'pets': pets, 'client': client})

def registerPet(request, id_cliente):
    client = Client.objects.get(pk=id_cliente)
    form = PetForm(request.POST, request.FILES)
    if form.is_valid():
        pet = form.save(commit=False)  # Guarda el formulario pero no lo inserta en la base de datos todavía
        pet.client_id = client  # Asigna el cliente a la mascota
        pet.save()  # Ahora guarda la mascota en la base de datos junto con el cliente
        return redirect(f'/homeClient/{client.client_id}')


    context = {
        'client': client,
        'form': form,
    }
    
    return render(request, 'registerPet.html', context)

def rateVet(request, appointment_id):
    appointment= Appointment.objects.filter(pk=appointment_id)
    if appointment and request.GET.get('rating')!=None:
        appointment.update(comment=request.GET.get('comment'))
        appointment.update(rating=request.GET.get('rating'))
        appointment= appointment[0]
    else:
        appointment= appointment[0]
    return render(request, 'rateVet.html',{'appointment':appointment,'client':appointment.pet_id.client_id})


def appointmentViewClient(request, id_pet):
    appointment= Appointment.objects.filter(pet_id=id_pet)
    return render(request,'appointmentViewClient.html',{'appointment':appointment})

def viewRate(request,client_id):
    pets=Pets.objects.filter(client_id=client_id)
    appointment=[]
    client=Client.objects.get(pk=client_id)
    for i in pets:
        appointment.append(Appointment.objects.filter(pet_id=i.pet_id)
                           .filter(date=datetime.now())
                           )
    
    return render(request,'viewRate.html',{'appointment':appointment,'client':client})


def vetInformation(request, id_cliente):
    client = Client.objects.get(pk=id_cliente)
    vet = Vet.objects.all()
    
    context = { 
        'client': client,
        'vet': vet,
    }
    
    return render(request, 'vetInformation.html', context)

def createAppointment(request, id_cliente):
    client = Client.objects.get(pk=id_cliente)
    
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

    return render(request, 'createAppointment.html', context)

        


