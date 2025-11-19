from django.db import models

class pessoa(models.Model): 
    
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    senha = models.CharField('Senha', max_length=30)
    telefone = models.CharField('Telefone', max_length=20)
    cpf = models.CharField('CPF', max_length=14)
    preferencias_animal = models.TextField('Preferências', null=True, blank=True)
    historico_adocoes = models.TextField('Histórico', null=True, blank=True)
    
    TIPO_RELACIONAMENTO = [
        ('A', 'Adotante'),
        ('D', 'Doador'),
        ('ADM', 'Administrador')
    ]
    
    tipo_relacionamento = models.CharField('Relacionamento', max_length=3, choices=TIPO_RELACIONAMENTO) 
    
    class Meta:
        verbose_name = 'pessoa' 
        verbose_name_plural = 'pessoas' 
        ordering =['id']

    def __str__(self):
        return self.nome