# Generated by Django 5.0.4 on 2024-04-14 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankrotApp', '0011_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма (руб.)')),
                ('location', models.CharField(max_length=255, verbose_name='Местонахождение')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankrotApp.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Наличные деньги',
                'verbose_name_plural': 'Наличные деньги',
            },
        ),
        migrations.CreateModel(
            name='Creditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('principal_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Чистая сумма (руб.)')),
                ('interest', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Проценты (руб.)')),
                ('court_fee', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Размер госпошлины (руб.)')),
                ('fines', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма штрафов (руб.)')),
                ('penalties', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма пеней (руб.)')),
                ('forfeits', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма неустоек (руб.)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankrotApp.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Кредитор',
                'verbose_name_plural': 'Кредиторы',
            },
        ),
        migrations.CreateModel(
            name='TaxDebt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Чистая сумма (руб.)')),
                ('fines', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Штрафы (руб.)')),
                ('penalties', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Пени (руб.)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankrotApp.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Долг по налогам',
                'verbose_name_plural': 'Долги по налогам',
            },
        ),
    ]
