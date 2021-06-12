from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import User as DefaultUser
from .models import Person, User

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_diplay = ('username', 'first_name', 'last_name', 'person', 'group', 'phone', 'email', 'date_joined')
    list_filter = ['person', 'date_joined']
    search_fields = ['username', 'email', 'phone']
