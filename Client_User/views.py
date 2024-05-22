from django.shortcuts import render, redirect
from django.utils.timezone import datetime
# Create your views here.
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
from django.http import HttpResponse
from .models import Report,File,Appointment,Client,Vet,Log_in,Pets
from .forms import ClientForm,Vetform

import requests
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
def choice(request):
    return render(request,"hello/choice.html",{'token':request.GET.get('access_token')})
def login(request):
    url = "https://justpetpals.com/api/v1/me"
    token=request.GET.get('access_token')
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        user=data.get('uuid')
        check= Log_in.objects.get(key=user)
    else:
        redirect("test")
    cost= Client.objects.filter(log_id=check)
    if(cost.first()!=None):
        return redirect('https://justpetpals.com/homeClient/'+str(cost.first().client_id)+"/?access_token="+token)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            
            client = form.save(commit=False)
            client.log_id = check # Assign the log_id from the URL to the form
            client.save()
            return redirect('https://justpetpals.com/homeClient/'+str(client.client_id)+"/?access_token="+token)  # Redirect to success page after successful form submission
    else:
        form = ClientForm()
    return render(request, "hello/login.html",{'form': form, 'log_id': check.log_id})
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
def choice(request):
    return render(request,"hello/choice.html",{'token':request.GET.get('access_token')})
def login2(request):
    url = "https://justpetpals.com/api/v1/me"
    token=request.GET.get('access_token')
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        user=data.get('uuid')
        check= Log_in.objects.get(key=user)
    else:
        redirect("test")
    cost= Vet.objects.filter(log_id=check)
    if(cost.first()!=None):
        return redirect('https://justpetpals.com/appointmentOutside/'+str(cost.first().vet_id)+"/?access_token="+token)
    if request.method == 'POST':
        form = Vetform(request.POST, request.FILES)
        if form.is_valid():
            
            client = form.save(commit=False)
            client.log_id = check # Assign the log_id from the URL to the form
            client.save()
            return redirect('https://justpetpals.com/appointmentOutside/'+str(client.vet_id)+"/?access_token="+token)  # Redirect to success page after successful form submission
    else:
        form = Vetform()
    return render(request, "hello/login2.html",{'form': form, 'log_id': check.log_id})

def appointmentCreate(request):
    return render(request,'hello/appointmentCreate.html')


def appointmentView(request):
    return render(request, 'hello/appointmentView.html')

def home(request):
    return render(request, "hello/home.html")
def about(request):
    return render(request, "hello/about.html")

def statistics(request):
    matplotlib.use('Agg')
    races = Pets.objects.values_list('race', flat=True).distinct().order_by('race')
    
    dog_counts_by_race = {}
    for race in races:
        if race:
            dogs_in_race = Pets.objects.filter(race=race)
        else:
            dogs_in_race = Pets.objects.filter(race__isnull=True)
            race = "None"
        count = dogs_in_race.count()
        dog_counts_by_race[race] = count

    bar_width = 0.5
    bar_positions = range(len(dog_counts_by_race))

    plt.figure(figsize=(10, 6))
    plt.bar(bar_positions, dog_counts_by_race.values(), width=bar_width, color='lightslategray', edgecolor='grey')

    plt.title('Registered Dogs by Types of Breed', fontsize=16, fontweight='bold')
    plt.xlabel('Breed', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Dogs', fontsize=14, fontweight='bold')

    plt.xticks(bar_positions, dog_counts_by_race.keys(), rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return render(request, "hello/statistics.html", {'graphic': graphic})