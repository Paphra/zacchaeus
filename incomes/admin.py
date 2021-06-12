from django.contrib import admin
from .models import Income, Interest, PropertyIncome

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']

@admin.register(PropertyIncome)
class PropertyIncomeAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']
