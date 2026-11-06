from django.urls import path
from ..views import paciente_views

urlpatterns = [
    path('', paciente_views.listar_pacientes, name='listar_pacientes'),
    path('novo/', paciente_views.criar_paciente, name='criar_paciente'),
    path('<int:pk>/editar/', paciente_views.editar_paciente, name='editar_paciente'),
    path('<int:pk>/excluir/', paciente_views.excluir_paciente, name='excluir_paciente'),
]