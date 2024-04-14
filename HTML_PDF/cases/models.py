from django.db import models
from django.contrib.auth.models import User
from bankrotApp.models import Car, Stock, TaxDebt, History, Client, Creditor, Cash, RealEstate, Account
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .utils import get_current_request

class Case(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    number = models.CharField(max_length=100, verbose_name="Номер дела", unique=True)
    cars = models.ManyToManyField(Car, verbose_name="Автомобили", blank=True)
    stocks = models.ManyToManyField(Stock, verbose_name="Акции/доли в обществах", blank=True)
    tax_debts = models.ManyToManyField(TaxDebt, verbose_name="Долги по налогам", blank=True)
    histories = models.ManyToManyField(History, verbose_name="Истории", blank=True)
    clients = models.ManyToManyField(Client, verbose_name="Клиенты", blank=True)
    creditors = models.ManyToManyField(Creditor, verbose_name="Кредиторы", blank=True)
    cash = models.ManyToManyField(Cash, verbose_name="Наличные деньги", blank=True)
    real_estate = models.ManyToManyField(RealEstate, verbose_name="Недвижимость", blank=True)
    accounts = models.ManyToManyField(Account, verbose_name="Счета", blank=True)

    class Meta:
        verbose_name = "Дело"
        verbose_name_plural = "Дела"

    def __str__(self):
        return self.number

@receiver(pre_save, sender=Case)
def add_user_to_case(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением