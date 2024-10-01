from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['client', 'amount', 'payment_date', 'method', 'category']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Выберите клиента'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Сумма'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'method': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Способ оплаты'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Категория'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].empty_label = "Выберите клиента"  # Пример метки для пустого значения