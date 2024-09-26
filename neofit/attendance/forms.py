from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['client', 'session', 'present']
        widgets = {
            'present': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }