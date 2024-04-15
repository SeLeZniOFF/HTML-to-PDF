from django.contrib import admin
from .models import DocumentForm

@admin.register(DocumentForm)
class DocumentFormAdmin(admin.ModelAdmin):
    list_display = ('case', 'template',)
    list_filter = ('case', 'template',)
    search_fields = ('case__number',)