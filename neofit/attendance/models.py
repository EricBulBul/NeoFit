from django.db import models
from appointments.models import Client, TrainingSession
from django.utils import timezone

class Attendance(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)  # Дата по умолчанию — текущая дата
    present = models.BooleanField(default=False)

    def present_status(self):
        return "Был" if self.present else "Не был"

    def __str__(self):
        return f"{self.client} - {self.session} ({self.date})"