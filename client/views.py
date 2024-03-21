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

def rateVet(request, id_client, vet_id):
    client=Client.objects.get(pk=id_client)
    vet_id= Vet.objects.get(pk=vet_id)
    appointment= Appointment.objects.filter(client_id=client).filter(vet_id=vet_id)
    if appointment and request.GET.get('rating')!=None:
        appointment.update(comment=request.GET.get('comment'))
        appointment.update(rating=request.GET.get('rating'))
        appointment=appointment[0]
    else:
        appointment=appointment.get(vet_id=vet_id)
    print(client.client_id)
    print(client)
    return render(request, 'rateVet.html',{'appointment':appointment,'client':client,'rate':appointment.rating,'com':appointment.comment})
def appointmentViewClient(request, id_pet):
    appointment= Appointment.objects.filter(pet_id=id_pet)
    return render(request,'appointmentViewClient.html',{'appointment':appointment})