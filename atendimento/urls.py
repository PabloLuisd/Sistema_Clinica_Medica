from django.urls import include, path
from .views.home_views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),

    path('pacientes/', include('atendimento.urls_configs.paciente_urls')),
    path('medicos/', include('atendimento.urls_configs.medico_urls')),
    path('especialidades/', include('atendimento.urls_configs.especialidade_urls')),
    path('consultas/', include('atendimento.urls_configs.consulta_urls')),
]