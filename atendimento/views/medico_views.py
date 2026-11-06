from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError

from ..models import Medico
from ..forms import MedicoForm


# Listar médicos
def listar_medicos(request):

    medicos = Medico.objects.select_related(
        'especialidade'
    ).order_by('nome')

    return render(request, 'atendimento/medicos/lista.html', {
        'medicos': medicos
    })


# Cadastrar médico
def criar_medico(request):

    form = MedicoForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            form.save()

            messages.success(request, 'Médico cadastrado com sucesso.')

            return redirect('listar_medicos')

    return render(request, 'atendimento/formulario.html', {
        'form': form,
        'titulo': 'Cadastrar médico',
        'voltar_url': 'listar_medicos'
    })


# Editar médico
def editar_medico(request, pk):

    medico = get_object_or_404(Medico, pk=pk)

    form = MedicoForm(request.POST or None, instance=medico)

    if request.method == 'POST':

        if form.is_valid():
            form.save()

            messages.success(request, 'Médico atualizado com sucesso.')

            return redirect('listar_medicos')

    return render(request, 'atendimento/formulario.html', {
        'form': form,
        'titulo': 'Editar médico',
        'voltar_url': 'listar_medicos'
    })


# Excluir médico
def excluir_medico(request, pk):

    medico = get_object_or_404(Medico, pk=pk)

    if request.method == 'POST':

        try:
            medico.delete()

            messages.success(request, 'Médico excluído com sucesso.')

        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir um médico que possui consultas.'
            )

        return redirect('listar_medicos')

    return render(request, 'atendimento/confirmar_exclusao.html', {
        'objeto': medico,
        'titulo': 'Excluir médico',
        'voltar_url': 'listar_medicos'
    })