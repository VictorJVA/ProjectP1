from django.db import models

# Create your models here.
class Client(models.Model):
    client_id= models.IntegerField(max_length=None,primary_key=True)
    log_id= models.ForeignKey('Log_in',on_delete=models.CASCADE,null=False)
    name= models.CharField(max_length=50)
    
class Pets(models.Model):
    pet_id= models.IntegerField(max_length= None,primary_key=True)
    client_id= models.ForeignKey('Client',on_delete=models.CASCADE,null=False)
    name=models.CharField(max_length=100, null=False)
    species=models.CharField(max_length=100, null=False)
    race=models.CharField(max_length=100, null= False)
    birth_date=models.DateField(max_length=99)
    gender= models.BooleanField()
    allergies=models.CharField(max_length=100, null= False)
    
class Medical_history(models.Model):
    Medical_history_id= models.IntegerField(max_length=None,primary_key=True)
    pet_id=models.ForeignKey('Pets',on_delete=models.CASCADE,null=False)
    
class Phone_Owner(models.Model):
    client_id= models.ForeignKey('Client',on_delete=models.CASCADE,null=False)
    country_intials=models.CharField(max_length=4)
    phone=models.CharField(max_length=15)
    
class Vaccination(models.Model):
    vaccination_id=models.IntegerField(max_length=None,primary_key=True)
    medical_history_id=models.ForeignKey('Medical_history',on_delete=models.CASCADE,null=False)
    vaccine=models.ForeignKey('Vaccines',on_delete=models.CASCADE,null=False)

class Vaccines(models.Model):
    vaccine_id=models.IntegerField(max_length=None,primary_key=True)
    vaccine_name= models.CharField(max_length=100, null=True)