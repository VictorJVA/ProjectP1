from django.contrib import admin
from .models import Log_in,Client,Vet,Appointment,Pets,Medical_history,Report,File
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.utils.translation import gettext_lazy as _

from Client_User.models import User
#-------------------------------------------------------------------------------
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'
        field_classes = {'username': UsernameField}


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', )}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )}
        ),
        (_('Important dates'), {'fields': ('created_at', 'updated_at', )}),
    )
    readonly_fields = ('created_at', 'updated_at', )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'email', 'password1', 'password2', ),
        }),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'is_staff', 'is_active', )
admin.site.register(Log_in)
admin.site.register(Client)
admin.site.register(Vet)
admin.site.register(Appointment)
admin.site.register(Pets)
admin.site.register(Medical_history)
admin.site.register(Report)
admin.site.register(File)