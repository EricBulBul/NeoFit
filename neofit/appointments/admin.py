from django.contrib import admin
from .models import Client, Trainer, TrainingSession, Appointment

admin.site.register(Client)
admin.site.register(Trainer)
admin.site.register(TrainingSession)
admin.site.register(Appointment)