# Generated by Django 5.0.4 on 2024-04-20 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankrotApp', '0018_arbitrationmanager'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arbitrationmanager',
            options={'verbose_name': 'Управляющий', 'verbose_name_plural': 'Управляющие'},
        ),
        migrations.AddField(
            model_name='arbitrationmanager',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Адрес'),
        ),
    ]