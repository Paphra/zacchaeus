from django.contrib import admin
from .models import Mail

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender_person', 'sender_user', 'receipient', 'read', 'date_sent')
    list_filter = ['sender_person', 'receipient', 'date_sent']
    search_fields = ['subject', 'sender_person', 'receipient', 'sender_user']
