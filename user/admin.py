from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets =((None, {"fields": ('username', 'password'),}),
                ('informacion personal',{"fields":('first_name', 'last_name', 'email','rh'),}),
                ('permisos',{"fields": ('is_active', 'is_staff','is_superuser', 'groups', 'user_permissions'),}),
                )
    list_display = [
                    'id',
                    'first_name',
                    'last_name',
                    'email',
                    'rh'
                    ]
    #pass