from django import forms
from .models import Asset, Debtor

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
        
class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
