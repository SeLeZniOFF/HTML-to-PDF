from django.urls import path
from .views import generate_document

urlpatterns = [
    path('generate-document/<int:form_id>/', generate_document, name='generate_document'),
]