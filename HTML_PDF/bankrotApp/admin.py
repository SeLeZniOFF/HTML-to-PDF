from django.contrib import admin
from .models import Client, Car, RealEstate, Account, Stock, Cash, Creditor,TaxDebt

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)

@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)

@admin.register(Cash)
class CashAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)

@admin.register(Creditor)
class CreditorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)

@admin.register(TaxDebt)
class TaxDebtAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)