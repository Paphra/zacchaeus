from django import forms
from sales.models import Sale, SalesReturn

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['business', 'user', 'particulars', 'details', 'amount', 'receipt', 'date_made']
        
class SalesReturnForm(forms.ModelForm):
    class Meta:
        model = SalesReturn
        fields = ['sale', 'particulars', 'details', 'amount', 'receipt', 'date_made']