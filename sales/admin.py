from django.contrib import admin
from .models import Sale, SalesReturn

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']

@admin.register(SalesReturn)
class SalesReturnAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']
