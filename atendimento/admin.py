from django.contrib import admin

# Register your models here.
from .models import Paciente, Medico, Consulta, Especialidade

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)
admin.site.register(Especialidade)