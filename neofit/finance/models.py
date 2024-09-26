from django.db import models
from appointments.models import Client

class Client(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    # Добавьте другие поля, если необходимо

class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    method = models.CharField(max_length=50)
    category = models.CharField(max_length=100, default="Без категории")  # Значение по умолчанию

    def __str__(self):
        return f"{self.client} - {self.amount} - {self.payment_date}"

