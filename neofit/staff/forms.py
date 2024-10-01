from django import forms
from .models import StaffMember

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'position', 'salary']  # Добавляем новые поля
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество (если есть)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        }
