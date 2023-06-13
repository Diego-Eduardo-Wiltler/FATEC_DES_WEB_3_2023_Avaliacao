from django.urls import path
from .views import RegistraPresenca, ListagemAlunos

urlpatterns = [
    path('', RegistraPresenca.as_view(), name='form'),
    path('lista_alunos', ListagemAlunos.as_view(), name='lista_alunos')
]
