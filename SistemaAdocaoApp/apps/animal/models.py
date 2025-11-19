from django.db import models
from ong.models import ong

# Create your models here.

class Animal(models.Model):
    #identificacao
    nome = models.CharField('Nome', max_length=50)
    especie = models.CharField('Espécie', max_length=30)
    raca = models.CharField('Raça', max_length=50, null=True, blank=True)
    
    #caracteristicas
    idade = models.IntegerField('Idade')
    sexo = models.CharField('Sexo', max_length=1, choices=[('M', 'Macho'), ('F', 'Fêmea')])
    descricao = models.TextField('Descrição Detalhada')
    
    STATUS_ANIMAL = [
        ('A', 'Aguardando Adoção'),
        ('D', 'Adotado'),
        ('R', 'Reservado')
    ]
    status = models.CharField('Status', max_length=1, choices=STATUS_ANIMAL, default='A')
    data_entrada = models.DateField('Data de Entrada no Abrigo')
    necessidades_especiais = models.TextField('Necessidades Especiais', null=True, blank=True)
    
    ong = models.ForeignKey(
        ong, 
        on_delete=models.CASCADE, 
        verbose_name='ong Responsável',
        related_name='animais' 
    ) 
    
    class Meta:
        verbose_name = 'animal'
        verbose_name_plural = 'animais'
        ordering =['nome']

    def __str__(self):
        return f"{self.nome} ({self.especie}) - {self.status}"