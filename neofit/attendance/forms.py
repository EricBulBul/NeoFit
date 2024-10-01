from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['client', 'session', 'present']
        labels = {
            'client': 'Клиент',
            'session': 'Тренировка',
            'present': 'Присутствие',
        }
        widgets = {
            'present': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }