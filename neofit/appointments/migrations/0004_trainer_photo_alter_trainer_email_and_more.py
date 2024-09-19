# Generated by Django 4.2.6 on 2024-09-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_rename_name_trainer_first_name_trainer_birthdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='trainer_photos/'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='gender',
            field=models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=10),
        ),
    ]
