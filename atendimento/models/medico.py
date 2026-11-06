from django.db import models
from .especialidade import Especialidade


class Medico(models.Model):
    nome = models.CharField(max_length=100)

    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.PROTECT,
        related_name='medicos'
    )

    crm = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome