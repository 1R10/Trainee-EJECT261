from django.db import models
from django.contrib.auth.models import AbstractUser
from .Validador_CPF import cpf_valido


class ContaPadrao(AbstractUser):
    #username      = None # Meu createsuperuser estava quebrando

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
    email         = models.EmailField(unique=True, blank= False)
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['nome_completo', 'nascimento', 'cpf']
    
    def validar(self):
        if cpf_valido(self.cpf) == False:
            raise ValueError('CPF inválido.') # Talvez exista um melhor para o django
        
    def saves(self, *args, **kwargs):
        self.username = self.email
        self.validar()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.nome_completo
    