# Generated by Django 5.0.4 on 2024-04-14 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankrotApp', '0003_car_realestate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=100, verbose_name='№ счета')),
                ('account_type', models.CharField(choices=[('current', 'Текущий'), ('checking', 'Расчетный'), ('credit', 'Кредитный'), ('deposit', 'Депозитный'), ('budget', 'Бюджетный'), ('social', 'Предназначенный для социальных выплат')], max_length=20, verbose_name='Вид счета')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Остаток в рублях')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
            },
        ),
    ]