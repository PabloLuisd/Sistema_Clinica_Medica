from django.urls import path
from ..views import medico_views

urlpatterns = [
    path('', medico_views.listar_medicos, name='listar_medicos'),
    path('novo/', medico_views.criar_medico, name='criar_medico'),
    path('<int:pk>/editar/', medico_views.editar_medico, name='editar_medico'),
    path('<int:pk>/excluir/', medico_views.excluir_medico, name='excluir_medico'),
]