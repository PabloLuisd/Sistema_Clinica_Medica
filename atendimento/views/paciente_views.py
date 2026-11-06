from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError

from ..models import Paciente
from ..forms import PacienteForm


# Listar pacientes
def listar_pacientes(request):

    pacientes = Paciente.objects.all().order_by('nome')

    return render(request, 'atendimento/pacientes/lista.html', {
        'pacientes': pacientes
    })


# Cadastrar paciente
def criar_paciente(request):

    form = PacienteForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            form.save()

            messages.success(request, 'Paciente cadastrado com sucesso.')

            return redirect('listar_pacientes')

    return render(request, 'atendimento/formulario.html', {
        'form': form,
        'titulo': 'Cadastrar paciente',
        'voltar_url': 'listar_pacientes'
    })


# Editar paciente
def editar_paciente(request, pk):

    paciente = get_object_or_404(Paciente, pk=pk)

    form = PacienteForm(request.POST or None, instance=paciente)

    if request.method == 'POST':

        if form.is_valid():
            form.save()

            messages.success(request, 'Paciente atualizado com sucesso.')

            return redirect('listar_pacientes')

    return render(request, 'atendimento/formulario.html', {
        'form': form,
        'titulo': 'Editar paciente',
        'voltar_url': 'listar_pacientes'
    })


# Excluir paciente
def excluir_paciente(request, pk):

    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':

        try:
            paciente.delete()

            messages.success(request, 'Paciente excluído com sucesso.')

        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir um paciente que possui consultas.'
            )

        return redirect('listar_pacientes')

    return render(request, 'atendimento/confirmar_exclusao.html', {
        'objeto': paciente,
        'titulo': 'Excluir paciente',
        'voltar_url': 'listar_pacientes'
    })