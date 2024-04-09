from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Client(models.Model):
    client_id= models.AutoField(max_length=None,primary_key=True)
    log_id= models.ForeignKey('Log_in',on_delete=models.CASCADE,null=False)
    name= models.CharField(max_length=50)
    postal_code=models.CharField(max_length=100)
    image= models.ImageField(upload_to='client/images/')

class Pets(models.Model):
    pet_id= models.AutoField(max_length= None,primary_key=True)
    client_id= models.ForeignKey('Client',on_delete=models.CASCADE,null=False)
    name=models.CharField(max_length=100, null=False)
    species=models.CharField(max_length=100, null=False)
    race=models.CharField(max_length=100, null= False)
    birth_date=models.DateField(max_length=99)
    gender= models.BooleanField()
    allergies=models.CharField(max_length=100, null= False)
    image= models.ImageField(upload_to='pet/images/')
    tipo_sangre= models.CharField(max_length=50, null= True)

    
class Medical_history(models.Model):
    Medical_history_id= models.AutoField(max_length=None,primary_key=True)
    pet_id=models.ForeignKey('Pets',on_delete=models.CASCADE,null=False)
    
class Phone_Owner(models.Model):
    client_id= models.ForeignKey('Client',on_delete=models.CASCADE,null=False)
    phone=models.CharField(max_length=15)
    
class Vaccination(models.Model):
    vaccination_id=models.AutoField(max_length=None,primary_key=True)
    medical_history_id=models.ForeignKey('Medical_history',on_delete=models.CASCADE,null=False)
    vaccine=models.ForeignKey('Vaccines',on_delete=models.CASCADE,null=False)
    vaccine_date= models.DateField(auto_now=False,auto_now_add=False,null=True)

class Vaccines(models.Model):
    vaccine_id=models.AutoField(max_length=None,primary_key=True)
    vaccine_name= models.CharField(max_length=100, null=True)


#QUICK SEPARATION
class Log_in(models.Model):
    log_id=models.AutoField(max_length=None,primary_key=True)
    user_name=models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    key=models.CharField(max_length=100,null=True)

class Vet(models.Model):
    vet_id=models.AutoField(max_length=None,primary_key=True)
    log_id=models.ForeignKey('Log_in',on_delete=models.CASCADE,null=False)
    name= models.CharField(max_length=50)
    postal_code=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    average_score=models.IntegerField()
    image= models.ImageField(upload_to='user/images/', null=True)
    address= models.CharField(max_length=100, null=True)
#QUICK SEPARATION
    


class Appointment(models.Model):
    appointment_id=models.AutoField(max_length=None,primary_key=True)
    pet_id= models.ForeignKey('Pets',on_delete=models.CASCADE,null=False)
    vet_id= models.ForeignKey('Vet',on_delete=models.CASCADE,null=False)
    date=models.DateField()
    time=models.TimeField(auto_now=False, auto_now_add=False)
    reason_appointment=models.CharField(max_length=200,null=True)
    rating=models.IntegerField(null=True)
    comment=models.CharField(max_length=50,null=True)
    appointment_accepted= models.BooleanField(default=False)


class Report(models.Model):
    report_id=models.AutoField(max_length=None,primary_key=True)
    appointement_id=models.ForeignKey('Appointment',on_delete=models.CASCADE,null=False)
    medical_history_id=models.ForeignKey('Medical_history',on_delete=models.CASCADE,null=False)
    test_findings=models.CharField(max_length=200, null=True)
    diagnosis=models.CharField(max_length=200, null=True)
    prescribed_treatment=models.CharField(max_length=200, null=True)
    recommendations=models.CharField(max_length=200, null=True)
    additional_note=models.CharField(max_length=200, null=True)
    update_note=models.CharField(max_length=100, null=False)
    date_created = models.DateField(auto_now_add=True)
    
class File(models.Model):    
    report_id=models.ForeignKey('Report',on_delete=models.CASCADE,null=False)
    file= models.FileField(upload_to ='medical/file/')