from django.db import models

# Create your models here.
class Pessoa(models.Model):
    TIPO_RELACIONAMENTO = [
        ('Adotante', 'Adotante'),
        ('Doador', 'Doador'),
        ('Administrador', 'Administrador'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    preferenciasAnimal = models.TextField(blank=True)
    historicoAdocoes = models.TextField(blank=True)
    tipoRelacionamento = models.CharField(max_length=20, choices=TIPO_RELACIONAMENTO)

    def __str__(self):
        return self.nome