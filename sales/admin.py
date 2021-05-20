from django.contrib import admin
from sales.models import Sale, SalesReturn

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'details', 'user', 'business', 'amount', 'date_made']
    list_filter = ['user', 'business', 'date_made']
    search_fields = ['particulars', 'details', 'amount']

@admin.register(SalesReturn)
class SalesReturnAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'details', 'sale', 'amount', 'date_made']
    list_filter = ['date_made']
    search_fields = ['particulars', 'details', 'amount']
