import random
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in, Pets
name= ["Caroline" ,"Khan","Kendrick", "Smith","Damien Reid","Charlee Pitts","Trey Tucker","Esther Solis"]
race= ["Dalmata","Plush Pug", "Mixed", "Bald","Bulldozer","Buldog","German Shepard"]
gender=["Male","Female"]
# for i in range(0,100):
#     log_in = Log_in(i,i,"RandomPass")
#     log_in.save()
for i in range(0,100):
    client = Client(i,i,name[random.randint(0, len(name)-1)],"media\client\images\WhatsApp_Image_2024-03-11_at_12.26.04_b1d3fe0c.jpg")
    client.save()
for i in range(0,100):
    pet= Pets(i,i,name[random.randint(0, len(name)-1)],'Dog',race[random.randint(0, len(race)-1)],"2024-3-12",gender[random.randint(0, len(gender)-1)],"Smth","media\pet\images\pet5_eGnd83u.jpg")
    pet.save()