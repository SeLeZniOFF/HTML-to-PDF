from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .utils import get_current_request

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    birth_date = models.DateField(verbose_name="Дата рождения")
    birth_place = models.CharField(max_length=100, verbose_name="Место рождения")
    snils = models.CharField(max_length=100, verbose_name="СНИЛС")
    inn = models.CharField(max_length=100, blank=True, null=True, verbose_name="ИНН")
    # Добавьте остальные атрибуты клиента здесь...

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_request().user
        super().save(*args, **kwargs)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    client = models.ManyToManyField(Client, blank=True, verbose_name="Клиент")
    brand = models.CharField(max_length=100, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год")
    number = models.CharField(max_length=20, verbose_name="Номер")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    location = models.CharField(max_length=100, verbose_name="Местонахождение")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    pledge_info = models.TextField(verbose_name="Сведения о залоге", blank=True, null=True)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f'{self.brand} {self.model} {", ".join(str(client) for client in self.client.all())}'

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_request().user
        super().save(*args, **kwargs)

class RealEstate(models.Model):
    PROPERTY_TYPES = [
        ('residential', 'Жилая недвижимость'),
        ('office', 'Офисная недвижимость'),
        ('warehouse', 'Складская недвижимость'),
        ('industrial', 'Промышленная недвижимость'),
        ('hotel', 'Гостиничная недвижимость'),
        ('commercial', 'Торговая недвижимость'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    client = models.ManyToManyField(Client, blank=True, verbose_name="Клиент")
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, verbose_name="Вид")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Площадь (кв.м)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    pledge_info = models.TextField(verbose_name="Сведения о залоге", blank=True, null=True)

    def __str__(self):
        clients_names = ", ".join(f"{client.last_name} {client.first_name}" for client in self.client.all())
        return f'{clients_names}, {self.address}'  # Отображаем имя и фамилию клиентов, затем адрес недвижимости

    class Meta:
        verbose_name = "Недвижимость"
        verbose_name_plural = "Недвижимость"

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_request().user
        super().save(*args, **kwargs)

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('current', 'Текущий'),
        ('checking', 'Расчетный'),
        ('credit', 'Кредитный'),
        ('deposit', 'Депозитный'),
        ('budget', 'Бюджетный'),
        ('social', 'Предназначенный для социальных выплат'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    client = models.ManyToManyField(Client, blank=True, verbose_name="Клиент")
    account_number = models.CharField(max_length=100, verbose_name="№ счета")
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, verbose_name="Вид счета")
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток в рублях")

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"

    def __str__(self):
        clients_names = ", ".join(f"{client.last_name} {client.first_name}" for client in self.client.all())
        return f'{clients_names}, {self.account_number}'  # Отображаем имя и фамилию клиентов, затем адрес недвижимости

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_request().user
        super().save(*args, **kwargs)

class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    organization_name = models.CharField(max_length=255, verbose_name="Наименование организации")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    authorized_capital = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Уставный капитал (руб.)")
    participation_share = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Доля участия")

    class Meta:
        verbose_name = "Акция/доля в обществе"
        verbose_name_plural = "Акции/доли в обществах"

    def __str__(self):
        return f'{self.client.last_name} {self.client.first_name}, {self.organization_name}'

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_request().user
        super().save(*args, **kwargs)

class Cash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма (руб.)")
    location = models.CharField(max_length=255, verbose_name="Местонахождение")

    class Meta:
        verbose_name = "Наличные деньги"
        verbose_name_plural = "Наличные деньги"

    def __str__(self):
        return f'{self.client.last_name} {self.client.first_name}, {self.amount}'

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_request().user
        super().save(*args, **kwargs)

class Creditor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    name = models.CharField(max_length=255, verbose_name="Наименование")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Чистая сумма (руб.)")
    interest = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Проценты (руб.)")
    court_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Размер госпошлины (руб.)")
    fines = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма штрафов (руб.)")
    penalties = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма пеней (руб.)")
    forfeits = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма неустоек (руб.)")

    @property
    def total_debt(self):
        return self.principal_amount + self.interest + self.court_fee + self.fines + self.penalties + self.forfeits

    class Meta:
        verbose_name = "Кредитор"
        verbose_name_plural = "Кредиторы"

    def __str__(self):
        return f'{self.client.last_name} {self.client.first_name}, {self.total_debt}'

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_request().user
        super().save(*args, **kwargs)

class TaxDebt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Чистая сумма (руб.)")
    fines = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Штрафы (руб.)")
    penalties = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Пени (руб.)")

    @property
    def total_amount(self):
        return self.principal_amount + self.fines + self.penalties

    class Meta:
        verbose_name = "Долг по налогам"
        verbose_name_plural = "Долги по налогам"

    def __str__(self):
        return f'{self.client.last_name} {self.client.first_name}, {self.total_amount}'

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_request().user
        super().save(*args, **kwargs)

# Сигналы для привязки пользователя к объекту перед сохранением
@receiver(pre_save, sender=Client)
def add_user_to_client(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением

@receiver(pre_save, sender=Car)
def add_user_to_car(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением

@receiver(pre_save, sender=RealEstate)
def add_user_to_real_estate(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением

@receiver(pre_save, sender=Account)
def add_user_to_account(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением

@receiver(pre_save, sender=Stock)
def add_user_to_stock(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением

@receiver(pre_save, sender=Cash)
def add_user_to_cash(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением

@receiver(pre_save, sender=Creditor)
def add_user_to_creditor(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением

@receiver(pre_save, sender=TaxDebt)
def add_user_to_taxDebt(sender, instance, **kwargs):
    if not instance.pk and not instance.user_id:
        instance.user = get_current_request().user  # Привязываем текущего пользователя к объекту перед сохранением
