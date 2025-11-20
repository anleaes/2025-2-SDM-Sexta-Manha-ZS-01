from django.db import models
from pessoa.models import pessoa
from ong.models import ong
from adocao.models import Adocao

class AgendamentoVisita(models.Model):
    # Atributos de Tempo e Local
    data_hora_visita = models.DateTimeField('Data e Hora da Visita')
    local_visita = models.CharField('Local da Visita', max_length=200)
    
    # Opções para o Status do Agendamento
    STATUS_AGENDAMENTO = [
        ('P', 'Pendente'),
        ('C', 'Confirmado'),
        ('R', 'Realizado'),
        ('A', 'Cancelado')
    ]
    status_agendamento = models.CharField('Status', max_length=1, choices=STATUS_AGENDAMENTO, default='P')
    
    # Observações e Feedback
    observacoes = models.TextField('Observações', null=True, blank=True)
    feedback_ong = models.TextField('Feedback da ONG', null=True, blank=True)
    
    solicitante = models.ForeignKey(
        pessoa,
        on_delete=models.CASCADE,
        verbose_name='Pessoa Solicitante',
        related_name='agendamentos_solicitados'
    )
    
    ong = models.ForeignKey(
        ong,
        on_delete=models.CASCADE,
        verbose_name='ONG Organizadora',
        related_name='agendamentos_organizados'
    )
    
    adocao = models.ForeignKey(
        Adocao,
        on_delete=models.CASCADE,
        verbose_name='Processo de Adoção Relacionado',
        related_name='agendamentos_visita'
    )
    
    class Meta:
        verbose_name = 'Agendamento de Visita'
        verbose_name_plural = 'Agendamentos de Visita'
        ordering = ['data_hora_visita']
        
    def __str__(self):
        return f"Agendamento para {self.solicitante.nome} em {self.data_hora_visita}"