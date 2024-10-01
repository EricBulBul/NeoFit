from django.db import models
from appointments.models import Client  # Импортируем модель Client из приложения appointments

class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Используем импортированную модель Client
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    method = models.CharField(max_length=50)
    category = models.CharField(max_length=100, default="Без категории")  # Значение по умолчанию

    def __str__(self):
        return f"{self.client} - {self.amount} - {self.payment_date}"
