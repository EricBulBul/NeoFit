from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Client(models.Model):
    last_name = models.CharField(max_length=100)  # Фамилия
    first_name = models.CharField(max_length=100)  # Имя
    middle_name = models.CharField(max_length=100, blank=True, null=True)  # Отчество (необязательно)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Номер телефона
    birthdate = models.DateField(null=True, blank=True)  # Дата рождения

    def __str__(self):
        return f'{self.last_name} {self.first_name}'



class Trainer(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    birthdate = models.DateField(null=True, blank=True)
    specialty = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Мужской'), ('female', 'Женский')])
    photo = models.ImageField(upload_to='trainer_photos/', blank=True, null=True)  # Поле для фото

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class TrainingSession(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.session}'
