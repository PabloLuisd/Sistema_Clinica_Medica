from django.urls import path
from ..views import especialidade_views

urlpatterns = [
    path('', especialidade_views.listar_especialidades, name='listar_especialidades'),
    path('nova/', especialidade_views.criar_especialidade, name='criar_especialidade'),
]