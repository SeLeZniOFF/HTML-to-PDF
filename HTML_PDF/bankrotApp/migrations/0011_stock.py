# Generated by Django 5.0.4 on 2024-04-14 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankrotApp', '0010_alter_client_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255, verbose_name='Наименование организации')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('authorized_capital', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Уставный капитал (руб.)')),
                ('participation_share', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Доля участия')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankrotApp.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Акция/доля в обществе',
                'verbose_name_plural': 'Акции/доли в обществах',
            },
        ),
    ]
