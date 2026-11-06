from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError

from ..models import Consulta
from ..forms import ConsultaForm


# Listar consultas
def listar_consultas(request):

    consultas = Consulta.objects.select_related(
        'paciente',
        'medico',
        'medico__especialidade'
    ).order_by('-data', '-horario')

    return render(request, 'atendimento/consultas/lista.html', {
        'consultas': consultas,
        'status_choices': Consulta.STATUS_CHOICES
    })


# Agendar consulta
def agendar_consulta(request):

    form = ConsultaForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            try:
                form.save()

                messages.success(
                    request,
                    'Consulta agendada com sucesso.'
                )

                return redirect('listar_consultas')

            except IntegrityError:
                form.add_error(
                    None,
                    'Este médico já possui uma consulta nesse horário.'
                )

    return render(request, 'atendimento/formulario.html', {
        'form': form,
        'titulo': 'Agendar consulta',
        'voltar_url': 'listar_consultas'
    })


# Alterar status da consulta
def alterar_status_consulta(request, pk):

    consulta = get_object_or_404(Consulta, pk=pk)

    if request.method == 'POST':

        novo_status = request.POST.get('status')

        status_validos = [
            opcao[0] for opcao in Consulta.STATUS_CHOICES
        ]

        if novo_status in status_validos:

            consulta.status = novo_status

            try:
                consulta.save()

                messages.success(
                    request,
                    'Status da consulta atualizado.'
                )

            except IntegrityError:
                messages.error(
                    request,
                    'Já existe uma consulta ativa para esse médico nesse horário.'
                )

        else:
            messages.error(request, 'Status inválido.')

    return redirect('listar_consultas')