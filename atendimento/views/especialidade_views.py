from django.shortcuts import render, redirect
from django.contrib import messages

from ..models import Especialidade
from ..forms import EspecialidadeForm


# Listar especialidades
def listar_especialidades(request):

    especialidades = Especialidade.objects.all().order_by('nome')

    return render(request, 'atendimento/especialidades/lista.html', {
        'especialidades': especialidades
    })


# Cadastrar especialidade
def criar_especialidade(request):

    form = EspecialidadeForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Especialidade cadastrada com sucesso.'
            )

            return redirect('listar_especialidades')

    return render(request, 'atendimento/formulario.html', {
        'form': form,
        'titulo': 'Cadastrar especialidade',
        'voltar_url': 'listar_especialidades'
    })