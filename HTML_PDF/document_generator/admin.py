from django.contrib import admin
from .models import DocumentForm,TemplateDocument

@admin.register(DocumentForm)
class DocumentFormAdmin(admin.ModelAdmin):
    list_display = ('case', 'template',)
    list_filter = ('case', 'template',)
    search_fields = ('case__number',)
@admin.register(TemplateDocument)
class TemplateDocumentAdmin(admin.ModelAdmin):
    pass