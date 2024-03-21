from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in, Pets
from django.shortcuts import render, redirect
from .forms import *
import pdb

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

def rateVet(request):
    return render(request, 'rateVet.html')