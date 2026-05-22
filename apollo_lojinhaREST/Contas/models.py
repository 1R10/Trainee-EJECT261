from django.db import models
from django.contrib.auth.models import AbstractUser


class ContaPadrao(AbstractUser):
    ROLE = (
        ('L', 'Lojista'),
        ('C', 'Cliente'),
    )
    role          = models.TextField(choices=ROLE, default='C')
    nome_completo = models.CharField(max_length=100, blank= False)
    nascimento    = models.DateField(blank= False)
    cpf           = models.CharField(max_length= 11, blank= False)
    telefone      = models.TextField(max_length= 14, blank= False) 
    cep           = models.TextField(max_length= 10, blank= False)
    endereco      = models.TextField( blank= False)
    REQUIRED_FIELDS = ['nome_completo', 'nascimento', 'cpf']
        #senha         = models.TextField(max_length= 50, blank= False) # min 8 car, 1 maiuscula 1 especial
        
    def __str__(self):
        return self.nome_completo