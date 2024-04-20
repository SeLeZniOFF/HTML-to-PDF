from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import Context, Template
from .models import DocumentForm


def generate_document(request, form_id):
    document_form = get_object_or_404(DocumentForm, id=form_id)  # Получаем форму документа по ID
    template = Template(document_form.template.html_code)  # Получаем HTML код шаблона
    context = {'case': document_form.case}  # Подготавливаем контекст для шаблона
    rendered_template = template.render(context)  # Рендерим шаблон с контекстом
    response = HttpResponse(rendered_template, content_type='text/html')  # Создаем HTTP ответ с сгенерированным HTML
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(document_form.template.name + '.html')
    return response
