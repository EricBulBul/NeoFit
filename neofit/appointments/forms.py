from django import forms
from .models import Client, Trainer, TrainingSession, Appointment

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email']

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'specialty']

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['title', 'description', 'date', 'trainer']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'session']
