# Generated by Django 5.0.4 on 2024-04-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankrotApp', '0008_account_client_car_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Фамилия'),
        ),
    ]