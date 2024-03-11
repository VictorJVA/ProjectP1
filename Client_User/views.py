from django.shortcuts import render, redirect
from django.utils.timezone import datetime
# Create your views here.
from django.http import HttpResponse
from .models import Report,File,Appointment,Client,Vet,Log_in

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def login(request):
    return render(request, "hello/login.html")

def appointmentCreate(request):
    return render(request,'hello/appointmentCreate.html')


def appointmentView(request):
    return render(request, 'hello/appointmentView.html')

def home(request):
    return render(request, "hello/home.html")
def about(request):
    return render(request, "hello/about.html")