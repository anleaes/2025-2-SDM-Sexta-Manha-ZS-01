from django.db import models

# Create your models here.

class ONG(models.Model):
    
    nome_instituicao = models.CharField('Nome da Instituição', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=25, unique=True) 
    endereco = models.CharField('Endereço', max_length=200)
    data_fundacao = models.DateField('Data de Fundação')
    
    class Meta:
        verbose_name = 'ONG'
        verbose_name_plural = 'ONGs'
        ordering =['nome_instituicao']

    def __str__(self):
        return self.nome_instituicao
    