from django import forms
from .models import Sale, SalesReturn

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
        
class SalesReturnForm(forms.ModelForm):
    class Meta:
        model = SalesReturn
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
