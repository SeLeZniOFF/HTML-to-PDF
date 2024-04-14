from django.contrib import admin
from .models import Case
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)  # Ограничиваем объекты только для текущего пользователя

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Запрещаем редактировать объекты, принадлежащие другим пользователям
        return super().has_change_permission(request, obj)