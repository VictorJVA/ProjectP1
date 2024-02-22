from django.shortcuts import render
from django.utils.timezone import datetime
# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "hello/home.html")

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

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")
def test1(request):
    return render(request,"travela-1.0.0/tour.html")

def menuUser(request):
    return render(request,"menu-bootstrap/a/menuUser.html")

def menuVet(request):
    return render(request,"menu-bootstrap/a/menuVet.html")