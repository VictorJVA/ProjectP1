import random
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in, Pets
name= ["Caroline" ,"Khan","Kendrick", "Smith","Damien Reid","Charlee Pitts","Trey Tucker","Esther Solis"]
race= ["Dalmata","Plush Pug", "Mixed", "Bald","Bulldozer","Buldog","German Shepard"]
gender=[True,False]
# for i in range(0,100):
#     log_in = Log_in(i,i,"RandomPass")
#     log_in.save()
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help= 'Generate dummy data'
    def handle(self,*args, **kwargs):
        for i in range(0,100):
            login=Log_in.objects.create(log_id=i,user_name=str(i),password=str(i),key=None)
            client=Client.objects.create(client_id=i,log_id=login,name=name[random.randint(0, len(name)-1)],postal_code=str(random.randint(40004,60004)),image="client/images/WhatsApp_Image_2024-03-11_at_12.26.04_b1d3fe0c_shD7I9H.jpg")
            Pets.objects.create(pet_id=i,client_id=client,name=name[random.randint(0, len(name)-1)],species='Dog',race=race[random.randint(0, len(race)-1)],birth_date="2024-3-12",gender=gender[random.randint(0, len(gender)-1)],allergies="Smth",image="pet/images/Alaska_6Zqr9ZT.jpg",tipo_sangre="DEA 1.1")
        