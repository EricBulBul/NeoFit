from django import forms
from .models import Client, Trainer, TrainingSession, Appointment
from datetime import timedelta

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'middle_name', 'email', 'phone_number', 'birthdate']
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'middle_name': 'Отчество (если есть)',
            'email': 'Электронная почта',
            'phone_number': 'Номер телефона',
            'birthdate': 'Дата рождения',
        }
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
        fields = ['last_name', 'first_name', 'middle_name', 'email', 'phone_number', 'birthdate', 'specialty', 'gender', 'photo']
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'middle_name': 'Отчество (если есть)',
            'email': 'Электронная почта',
            'phone_number': 'Номер телефона',
            'birthdate': 'Дата рождения',
            'specialty': 'Специальность',
            'gender': 'Пол',
            'photo': 'Фото',
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['title', 'description', 'date', 'time', 'end_time', 'type', 'max_participants', 'trainer']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'date': 'Дата',
            'time': 'Время начала',
            'end_time': 'Время окончания',
            'type': 'Тип',
            'max_participants': 'Макс. количество участников',
            'trainer': 'Тренер',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'session']
        labels = {
            'client': 'Клиент',
            'session': 'Тренировка',
        }

