from django.db import models
from cases.models import Case

class TemplateDocument(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название шаблона")
    html_code = models.TextField(verbose_name="HTML код шаблона")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Шаблон отчета"
        verbose_name_plural = "Шаблоны отчетов"
class DocumentForm(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name="Дело")
    template = models.ForeignKey(TemplateDocument, on_delete=models.CASCADE, verbose_name="Шаблон документа")

    class Meta:
        verbose_name = "Скачивание отчета"
        verbose_name_plural = "Скачивание отчетов"

    def __str__(self):
        return f"Документ для дела {self.case.number}"
