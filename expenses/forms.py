from django import forms
from .models import Expense, Depreciation

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']

class DepreciationForm(forms.ModelForm):
    class Meta:
        model = Depreciation
        fields = ['person', 'user', 'particulars', 'details', 'amount', 'receipt', 'document', 'date_made']
