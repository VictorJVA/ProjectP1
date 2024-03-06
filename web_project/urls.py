from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import os
"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from hello import views as views
from client import views as client
from user import views as user
from web_project import views as project

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", project.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", project.about, name="about"),
    path('admin/', admin.site.urls),
    path('appoint/<appointment>/',user.backtest,name="appointment"),
    path("login/", views.login),
    path("appointmentView/", views.appointmentView, name="appointmentView"),
    path("appointmentCreate/", views.appointmentCreate,name ="appointmentCreate"),
    path("rateVet/", client.rateVet, name = "rateVet"),
    path("petView/",user.viewPets,name= "viewPets"),
    path("homeClient/",client.homeClient,name= "homeClient"),
    path('save/',views.save,name='save'),
]

urlpatterns += static('/report/',document_root=os.path.join(BASE_DIR,'report'))
