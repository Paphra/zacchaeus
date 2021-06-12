from django.contrib import admin
from .models import Asset, Debtor

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']

@admin.register(Debtor)
class DebtorAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']
