from django.db import models
from django.db.models import Q

from .paciente import Paciente
from .medico import Medico


class Consulta(models.Model):

    STATUS_CHOICES = [
        ('Agendada', 'Agendada'),
        ('Realizada', 'Realizada'),
        ('Cancelada', 'Cancelada'),
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        related_name='consultas'
    )

    medico = models.ForeignKey(
        Medico,
        on_delete=models.PROTECT,
        related_name='consultas'
    )

    data = models.DateField()
    horario = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Agendada'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['medico', 'data', 'horario'],
                condition=~Q(status='Cancelada'),
                name='consulta_medico_horario_ativo_unico'
            )
        ]

    def __str__(self):
        return f'{self.paciente} - {self.medico} - {self.data}'