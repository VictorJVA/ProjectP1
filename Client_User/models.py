# Create your models here.
from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

class AbstractBaseModel(models.Model):
    """
    Base abstract model, that has `uuid` instead of `id` and includes `created_at`, `updated_at` fields.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        abstract = True
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'

class User(PermissionsMixin, AbstractBaseUser, AbstractBaseModel):
    """
    Table contains cognito-users & django-users.
    PermissionsMixin leverage built-in django model permissions system
    (which allows to limit information for staff users via Groups).
    Note: Django-admin user and app user not split in different tables because of simplicity of development.
    Some libraries assume there is only one user model, and they can't work with both.
    For example to have a history log of changes for entities - to save which user made a change of object attribute,
    perhaps, auth-related libs, and some other.
    With current implementation we don't need to fork, adapt and maintain third party packages.
    They should work out of the box.
    The disadvantage is - cognito-users will have unused fields which always empty. Not critical.
    """
    username_validator = UnicodeUsernameValidator()

    ### Common fields ###
    # For cognito-users username will contain `sub` claim from jwt token
    # (unique identifier (UUID) for the authenticated user).
    # For django-users it will contain username which will be used to login into django-admin site
    username = models.CharField('Username', max_length=255, unique=True, validators=[username_validator])
    is_active = models.BooleanField('Active', default=True)

    ### Cognito-user related fields ###
    # some additional fields which will be filled-out only for users registered via Cognito
    

    ### Django-user related fields ###
    # password is inherited from AbstractBaseUser
    email = models.EmailField('Email address', blank=True)  # allow non-unique emails
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.'
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']  # used only on createsuperuser

    @property
    def is_django_user(self):
        return self.has_usable_password()
    


#Sep--------------------------------------------------------------------------------------------------------------------------
class Client(models.Model):
    client_id= models.AutoField(max_length=None,primary_key=True)
    log_id= models.ForeignKey('Log_in',on_delete=models.CASCADE,null=False)
    name= models.CharField(max_length=50)
    postal_code=models.CharField(max_length=100)
    image= models.ImageField(upload_to='client/images/')
    def __str__(self):
        return self.name

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
    def __str__(self):
        return self.name

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
    key=models.CharField(max_length=100,null=True)


class Vet(models.Model):
    vet_id=models.AutoField(max_length=None,primary_key=True)
    log_id=models.ForeignKey('Log_in',on_delete=models.CASCADE,null=False)
    name= models.CharField(max_length=50)
    postal_code=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    average_score=models.IntegerField(null=True)
    image= models.ImageField(upload_to='user/images/', null=True)
    address= models.CharField(max_length=100, null=True)
#QUICK SEPARATION
    def __str__(self):
        return self.name


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