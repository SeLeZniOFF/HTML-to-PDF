# Generated by Django 5.0.4 on 2024-04-14 20:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bankrotApp', '0017_alter_history_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, unique=True, verbose_name='Номер дела')),
                ('accounts', models.ManyToManyField(blank=True, to='bankrotApp.account', verbose_name='Счета')),
                ('cars', models.ManyToManyField(blank=True, to='bankrotApp.car', verbose_name='Автомобили')),
                ('cash', models.ManyToManyField(blank=True, to='bankrotApp.cash', verbose_name='Наличные деньги')),
                ('clients', models.ManyToManyField(blank=True, to='bankrotApp.client', verbose_name='Клиенты')),
                ('creditors', models.ManyToManyField(blank=True, to='bankrotApp.creditor', verbose_name='Кредиторы')),
                ('histories', models.ManyToManyField(blank=True, to='bankrotApp.history', verbose_name='Истории')),
                ('real_estate', models.ManyToManyField(blank=True, to='bankrotApp.realestate', verbose_name='Недвижимость')),
                ('stocks', models.ManyToManyField(blank=True, to='bankrotApp.stock', verbose_name='Акции/доли в обществах')),
                ('tax_debts', models.ManyToManyField(blank=True, to='bankrotApp.taxdebt', verbose_name='Долги по налогам')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Дело',
                'verbose_name_plural': 'Дела',
            },
        ),
    ]