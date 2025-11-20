from django.db import models
from campanha.models import Campanha 
from pessoa.models import pessoa   

# Create your models here.


class Pagamento(models.Model):
    
    valor = models.DecimalField('Valor da Doação', max_digits=10, decimal_places=2)
    data_pagamento = models.DateField('Data do Pagamento')
    
    FORMA_PAGAMENTO = [
        ('PIX', 'Pix'),
        ('CC', 'Cartão de Crédito'),
        ('BO', 'Boleto'),
        ('TR', 'Transferência')
    ]
    forma_pagamento = models.CharField('Forma de Pagamento', max_length=3, choices=FORMA_PAGAMENTO)
    
    comprovante_url = models.CharField('URL do Comprovante', max_length=255, null=True, blank=True)
    
    
    campanha = models.ForeignKey(
        Campanha,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        verbose_name='Campanha Destino',
        related_name='doacoes_recebidas'
    )
    
    doador = models.ForeignKey(
        pessoa,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        verbose_name='Doador',
        related_name='doacoes_realizadas'
    )
    class Meta:
        verbose_name = 'Pagamento de Doação'
        verbose_name_plural = 'Pagamentos de Doações'
        ordering = ['-data_pagamento'] 
        
    def __str__(self):
        return f"R$ {self.valor} - {self.get_forma_pagamento_display()}"
