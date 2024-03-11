from django.shortcuts import render
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in
from django.shortcuts import render, redirect

def homeClient(request):
    return render(request, 'homeClient.html')

def registerPet(request):
    return render(request, 'registerPet.html')

def rateVet(request):
    return render(request, 'rateVet.html')