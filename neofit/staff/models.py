from django.db import models


class StaffMember(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество(если есть)")  # Отчество (необязательно)
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Телефон")

    # Новые поля
    position = models.CharField(max_length=100, verbose_name="Должность")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Зарплата")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"
