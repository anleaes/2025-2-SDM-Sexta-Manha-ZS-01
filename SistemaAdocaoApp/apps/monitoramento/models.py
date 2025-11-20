from django.db import models
from adocao.models import Adocao

# Create your models here.

class MonitoramentoPosAdocao(models.Model):
    data_visita = models.DateField('Data da Visita/Verificação')
    
    STATUS_SAUDE = [
        ('E', 'Excelente'),
        ('B', 'Bom'),
        ('R', 'Requer Atenção'),
        ('C', 'Crítico')
    ]
    status_saude = models.CharField('Status de Saúde do Animal', max_length=1, choices=STATUS_SAUDE, default='B')
    
    condicoes_ambientais = models.TextField('Condições do Ambiente', help_text='Descrição do lar, higiene, espaço disponível.')
    
    observacoes = models.TextField('Observações do Monitor', null=True, blank=True)
    
    RESULTADO_MONITORAMENTO = [
        ('S', 'Satisfatório'),
        ('I', 'Insatisfatório (Requer Ação)')
    ]
    resultado = models.CharField('Resultado', max_length=1, choices=RESULTADO_MONITORAMENTO, default='S')
    
    adocao = models.ForeignKey(
        Adocao,
        on_delete=models.CASCADE, 
        verbose_name='Processo de Adoção Relacionado',
        related_name='monitoramento' 
    )
    
    class Meta:
        verbose_name = 'Monitoramento Pós-Adoção'
        verbose_name_plural = 'Monitoramentos Pós-Adoção'
        ordering = ['-data_visita']
        
    def __str__(self):
        return f"Monitoramento da Adoção {self.adocao.id} - Data: {self.data_visita}"