from django.contrib import admin
from .models import Log_in,Client,Vet,Appointment,Pets,Medical_history,Report,File
# Register your models here.
admin.site.register(Log_in)
admin.site.register(Client)
admin.site.register(Vet)
admin.site.register(Appointment)
admin.site.register(Pets)
admin.site.register(Medical_history)
admin.site.register(Report)
admin.site.register(File)