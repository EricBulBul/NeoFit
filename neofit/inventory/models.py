from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    condition = models.CharField(max_length=100, default="Новый", verbose_name="Состояние")
    purchase_date = models.DateField(null=True, blank=True, verbose_name="Дата приобретения")

    def __str__(self):
        return f"{self.name} - {self.quantity} шт."