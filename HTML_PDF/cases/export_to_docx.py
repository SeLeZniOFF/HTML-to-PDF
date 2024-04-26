import os
import zipfile

from django.http import FileResponse
from docx import Document
from docx.shared import Pt

from .models import Case


def export_to_docx(request):
    data = request.POST
    case_ids = data.getlist('_selected_action')
    cases = Case.objects.filter(id__in=case_ids)

    document_path_list = ['static/letter.docx']
    documents = []
    response = []
    
    for case in cases:
        for document_path in document_path_list:
            document = Document(document_path)

            for paragraph in document.paragraphs:
                paragraph.text = paragraph.text.replace(
                    '{{ manager.first_name }} {{ manager.last_name }} {{ manager.middle_name }}',
                    f'{case.manager.first_name} {case.manager.last_name} {case.manager.middle_name}'
                )
                paragraph.text = paragraph.text.replace('{{ manager.address }}', case.manager.address)
                paragraph.text = paragraph.text.replace('{{ case.case_number }}.', case.number)

                result = ', '.join([str(client) for client in case.clients.all()])
                paragraph.text = paragraph.text.replace(
                    '{{ client.first_name }} {{ client.last_name }} {{ client.middle_name }} ',
                    result
                )

                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(13)

            document.save(f'static/{case.number}.docx')
            documents.append(document)
        
        zip_file_name = os.path.join('static/', 'documents.zip')
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            for case in cases:
                file_name = f'{case.number}.docx'
                if file_name in os.listdir('static/'):
                    zip_file.write(os.path.join('static/', file_name), arcname=file_name)

        
        response = FileResponse(open(zip_file_name, 'rb'), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="documents.zip"'
    return response
