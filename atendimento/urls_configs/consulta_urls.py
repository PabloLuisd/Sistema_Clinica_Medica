from django.urls import path
from ..views import consulta_views

urlpatterns = [
    path('', consulta_views.listar_consultas, name='listar_consultas'),
    path('agendar/', consulta_views.agendar_consulta, name='agendar_consulta'),
    path('<int:pk>/status/', consulta_views.alterar_status_consulta, name='alterar_status_consulta'),
]