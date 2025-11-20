from django.db import models
from pessoa.models import pessoa
from animal.models import Animal

# Create your models here.
    
class Adocao(models.Model):
        
    data_solicitacao = models.DateField('Data da Solicitação', auto_now_add=True)
    data_conclusao = models.DateField('Data da Conclusão', null=True, blank=True)
    
    STATUS_ADOCAO = [
        ('S', 'Solicitada'),
        ('E', 'Em Avaliação'),
        ('A', 'Aprovada'),
        ('C', 'Concluída'),
        ('R', 'Rejeitada')
    ]
    status = models.CharField('Status', max_length=1, choices=STATUS_ADOCAO, default='S')
    requer_documentos = models.BooleanField('Requer Documentos', default=True)
    observacoes = models.TextField('Observações', null=True, blank=True)

   
    solicitante = models.ForeignKey(
        pessoa, 
        on_delete=models.CASCADE, 
        verbose_name='Pessoa Solicitante',
        related_name='solicitacoes_adocao'
    ) 

    animal = models.OneToOneField(
        Animal, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name='Animal Envolvido'
    ) 
    
    class Meta:
        verbose_name = 'Adoção'
        verbose_name_plural = 'Adoções'
        ordering =['-data_solicitacao']

    def __str__(self):
        return f"Adoção {self.pk} - {self.solicitante.nome} - Status: {self.get_status_display()}"