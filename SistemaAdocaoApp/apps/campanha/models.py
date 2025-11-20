from django.db import models
from ong.models import ong

# Create your models here.

class Campanha(models.Model):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição')
    
    data_inicio = models.DateField('Data Início')
    data_fim = models.DateField('Data Fim')
    local = models.CharField('Local', max_length=100)
    
    meta_doacao = models.DecimalField('Meta de Doação', max_digits=10, decimal_places=2)
    
    STATUS_CAMPANHA = [
        ('A', 'Ativa'),
        ('F', 'Finalizada'),
        ('C', 'Cancelada')
    ]
    status = models.CharField('Status', max_length=1, choices=STATUS_CAMPANHA, default='A')
    
    tipo_campanha = models.CharField('Tipo de Campanha', max_length=50) 
    
    ong = models.ForeignKey(
        ong,
        on_delete=models.CASCADE,
        verbose_name='ONG Organizadora',
        related_name='campanhas'
    )
    
    class Meta:
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'
        ordering = ['-data_inicio']
        
    def __str__(self):
        return f"{self.titulo} ({self.get_status_display()})"