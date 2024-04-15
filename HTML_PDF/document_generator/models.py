from django.db import models
from cases.models import Case
from cases.models import TemplateDocument

class DocumentForm(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name="Дело")
    template = models.ForeignKey(TemplateDocument, on_delete=models.CASCADE, verbose_name="Шаблон документа")

    class Meta:
        verbose_name = "Скачивание отчета"
        verbose_name_plural = "Скачивание отчетов"

    def __str__(self):
        return f"Документ для дела {self.case.number}"