from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'condition', 'purchase_date']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'})
        }
