from django import forms
from .models import Mail

class MailForm(forms.ModelForm):
	class Meta:
		model = Mail
		fields = ['subject', 'body', 'sender_person', 'sender_user', 'receipient', 'attachment']
		