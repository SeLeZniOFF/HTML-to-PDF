# Generated by Django 5.0.4 on 2024-04-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankrotApp', '0009_client_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
    ]
