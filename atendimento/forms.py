from django import forms

from .models import (
    Paciente,
    Medico,
    Especialidade,
    Consulta
)


# Formulário de Paciente
class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente

        fields = [
            'nome',
            'cpf',
            'data_nascimento',
            'telefone'
        ]

        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date'}
            )
        }


# Formulário de Médico
class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico

        fields = [
            'nome',
            'especialidade',
            'crm',
            'telefone'
        ]


# Formulário de Especialidade
class EspecialidadeForm(forms.ModelForm):

    class Meta:
        model = Especialidade

        fields = [
            'nome',
            'descricao'
        ]


# Formulário de Consulta
class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta

        fields = [
            'paciente',
            'medico',
            'data',
            'horario'
        ]

        widgets = {
            'data': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'horario': forms.TimeInput(
                attrs={'type': 'time'}
            )
        }

    # Verifica se o médico já possui uma consulta
    # no mesmo dia e horário
    def clean(self):

        dados = super().clean()

        medico = dados.get('medico')
        data = dados.get('data')
        horario = dados.get('horario')

        if medico and data and horario:

            conflito = Consulta.objects.filter(
                medico=medico,
                data=data,
                horario=horario
            ).exclude(status='Cancelada')

            # Na edição, ignora a própria consulta
            if self.instance.pk:
                conflito = conflito.exclude(
                    pk=self.instance.pk
                )

            if conflito.exists():
                raise forms.ValidationError(
                    'Este médico já possui uma consulta '
                    'agendada para essa data e horário.'
                )

        return dados