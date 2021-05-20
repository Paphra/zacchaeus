from django.contrib import admin
from purchases.models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass
