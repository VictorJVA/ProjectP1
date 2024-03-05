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

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('admin/', admin.site.urls),
    path("menuUser/",views.menuUser,name="menuUser"),
    path("menuVet/",views.menuVet,name="menuVet"),
    path('appoint/<appointment>/',views.backtest,name="appointment"),
    path("login/", views.login),
    path("appointmentView/", views.appointmentView, name="appointmentView"),
    path("appointmentCreate/", views.appointmentCreate,name ="appointmentCreate"),
    path("rateVet/", views.rateVet, name = "rateVet"),
    path("petView/",views.viewPets,name= "viewPets"),
    path("save/",views.saved,name="save")
,
    path("menu/",views.menu,name= "Menu")
]

urlpatterns += static('/report/',document_root=os.path.join(BASE_DIR,'report'))
