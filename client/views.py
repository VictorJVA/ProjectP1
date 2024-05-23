from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in, Pets
from django.shortcuts import render, redirect
from .forms import *
import pdb
from datetime import datetime

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from web_project.api.UserSerializer import UserSerializer

#----------------------------------------------------------------------------------------------
import requests
def PetView(request, client_id, pet_id):
    pet=Pets.objects.get(pk=pet_id)
    client=Client.objects.get(client_id=client_id)
    
    if(pet.client_id.client_id==client_id):
        pet = Pets.objects.filter(pet_id=pet_id) 

    return render(request, 'clinicalUserView2.html', {'pets': pet,'client':client})
def my_view(request):
    url = "https://www.justpetpals.com/api/v1/me"  # Your API endpoint
    jwt_token=None
    jwt_token = request.GET.get('access_token')
    headers = {
        "Authorization": f"Bearer {jwt_token}"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data.get('uuid'))
        user=data.get('uuid')
        check= Log_in.objects.filter(key=user).first()
        print(data)
        if check==None:
            Log_in.objects.create(key=user)
            return redirect("/choice/?access_token="+jwt_token)
        else:
            return redirect("/choice/?access_token="+jwt_token)
    else:
        data=None
    return render(request, 'test.html', {'data': data,'token':jwt_token})

#----------------------authtest

class UserProfileAPIView(RetrieveModelMixin, GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        
        """
        User profile
        Get profile of current logged in user.
        """
        return self.retrieve(request, *args, **kwargs)

#------------------------auth

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
        Medical_history.objects.create(pet_id=pet)
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
    pets = Pets.objects.filter(client_id=client)
    
    
    appointment = []
    for i in pets:
        appointment.append(Appointment.objects.filter(pet_id=i.pet_id).filter(date__gte = datetime.now()))
    
    if request.method == 'POST':
        form = AppointmentForm(client_id=id_cliente, data=request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            date = form.cleaned_data['date']
            vet = form.cleaned_data['vet_id']
            accepted = Appointment.objects.filter(appointment_accepted = False).filter(vet_id=vet).filter(date = date).filter(time = time)
            # print(accepted.first())
            # fecha_objeto = datetime.strptime(date, "%Y-%m-%d")
            if (accepted.first() != None or date < datetime.now().date()):
                context = { 
                        'form': form,
                        'client':client,
                        'accepted':True,
                        'appointment': appointment,
                        }
                return render(request, 'createAppointment.html', context)
            
            form.save()
            # Aquí podrías agregar un mensaje de éxito o realizar cualquier otra acción necesaria
            form = AppointmentForm(client_id=id_cliente)  # Vaciar el formulario después de enviar los datos exitosamente
    else:
        form = AppointmentForm(client_id= id_cliente)

    context = {
        'form': form,
        'client':client,
        'appointment': appointment,
        
    }
    # pdb.set_trace()

    return render(request, 'createAppointment.html', context)


def vetProfile(request, id_cliente, vet_id):
    vet = Vet.objects.get(pk=vet_id)
    client = get_object_or_404(Client, pk=id_cliente)
    context = { 
        'vet': vet,
        'client': client,
    }
    return render(request, 'vetProfile.html', context)