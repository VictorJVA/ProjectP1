from django.db import models

# Create your models here.
class Vet(models.Model):
    vet_id=models.IntegerField(max_length=None,primary_key=True)
    log_id=models.ForeignKey('Log_in',on_delete=models.CASCADE,null=False)
    name= models.CharField(max_length=50)
    country_intials=models.CharField(max_length=4)
    phone=models.CharField(max_length=15)
