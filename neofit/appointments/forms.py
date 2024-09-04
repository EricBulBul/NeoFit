from django import forms
from .models import Client, Trainer, TrainingSession, Appointment

from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'middle_name', 'email', 'phone_number', 'birthdate']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество (если есть)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Дата рождения', 'type': 'date'}),
        }


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['last_name', 'first_name', 'middle_name', 'email', 'phone_number', 'birthdate', 'specialty', 'gender']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество (если есть)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Дата рождения', 'type': 'date'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Специальность'}),
            'gender': forms.Select(choices=[('M', 'Мужской'), ('F', 'Женский')], attrs={'class': 'form-control'}),
        }

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['title', 'description', 'date', 'trainer']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'session']
