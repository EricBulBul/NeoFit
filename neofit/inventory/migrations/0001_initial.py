# Generated by Django 4.2.7 on 2024-09-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('condition', models.CharField(default='Новый', max_length=100)),
                ('purchase_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
