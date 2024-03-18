from django.shortcuts import render, get_object_or_404
from django.http import Http404
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in, Pets
from django.shortcuts import render, redirect
import pdb

def homeClient(request, id_cliente):

    client = Client.objects.get(pk=id_cliente)
    pets = Pets.objects.filter(client_id=client)
    print(pets)
    # pdb.set_trace()
    return render(request, 'homeClient.html', {'pets': pets, 'client': client}, {'pets': pets, 'client': client})

def registerPet(request):
    return render(request, 'registerPet.html')

def rateVet(request):
    return render(request, 'rateVet.html')

def appointmentViewClient(request,id_pet):
    appointment = Appointment.objects.filter(pet_id=id_pet)
    client = Pets.objects.get(pk=id_pet).client_id
    # pdb.set_trace()
    return render(request, 'appointmentViewClient.html', {'appointment': appointment, 'client': client})