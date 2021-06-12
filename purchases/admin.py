from django.contrib import admin
from .models import Purchase, PurchasesReturn

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']

@admin.register(PurchasesReturn)
class PurchasesReturnAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']
