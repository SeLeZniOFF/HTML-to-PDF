from django.contrib import admin
from django.http import HttpResponse
from docx import Document

from .export_to_docx import export_to_docx
from .models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):

    list_display = ('id', 'number', 'user')
    search_fields = ('id', 'number')
    list_filter = ('user',)
    readonly_fields = ('id',)
    actions = ['export_to_docx']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return super().has_change_permission(request, obj)
    
    def export_to_docx(self, request, queryset):
        doc = export_to_docx(request)
        return doc
    export_to_docx.short_description = 'Экспорт в DOC'
