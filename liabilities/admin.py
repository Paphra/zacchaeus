from django.contrib import admin
from .models import Liability, Creditor, Withdrawal

@admin.register(Liability)
class LiabilityAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']

@admin.register(Creditor)
class CreditorAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']

@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ['particulars', 'user', 'person', 'amount', 'date_made']
    list_filter = ['person', 'date_made', 'user']
    search_fields = ['particulars', 'details', 'amount']
