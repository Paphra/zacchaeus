from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Business, Address, Size, Directorship

admin.site.register(User, UserAdmin)

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass

@admin.register(Directorship)
class DirectorshipAdmin(admin.ModelAdmin):
    pass
