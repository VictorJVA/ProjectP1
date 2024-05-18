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

def stastistics(request):
    matplotlib.use('Agg')
    years= Pets.objects.values_list('race', flat=True).distinct().order_by('race')
    
    movie_counts_by_year= {}
    for year in years:
        if year:
            movies_in_year=  Pets.objects.filter(race=year)
        else:
             movies_in_year= Pets.objects.filter(race__isnull=True)
             year="None"
        count=movies_in_year.count()
        movie_counts_by_year[year]=count
    bar_width=0.5
    bar_positions = range(len(movie_counts_by_year))
    

    plt.bar(bar_positions ,movie_counts_by_year.values() , width=bar_width, align='center')
    
    plt.title('Registered dogs by types of breed')
    plt.xlabel('Breed')
    plt.ylabel('Number of dogs')
    
    plt.xticks(bar_positions, movie_counts_by_year.keys(),rotation=90)
    
    plt.subplots_adjust(bottom=0.3)
    
    buffer= io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_png= buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic=graphic.decode('utf-8')
    return render(request,"hello/statistics.html",{'graphic':graphic})