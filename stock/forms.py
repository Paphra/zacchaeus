from django import forms
from .models import ClosingStock, OpeningStock

class ClosingForm(forms.ModelForm):
    class Meta:
        model = ClosingStock
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'document', 'date_made']
        
class OpeningForm(forms.ModelForm):
    class Meta:
        model = OpeningStock
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'document', 'date_made']
