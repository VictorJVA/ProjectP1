from django.shortcuts import render, redirect
from django.utils.timezone import datetime
# Create your views here.
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
from django.http import HttpResponse
from .models import Report,File,Appointment,Client,Vet,Log_in,Pets

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