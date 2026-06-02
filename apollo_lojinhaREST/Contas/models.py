from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.core.validators import MinLengthValidator


class ContaPadrao(AbstractUser):
    ROLE = (
        ('L', 'Lojista'),
        ('C', 'Cliente'),
    )
    role          = models.TextField(choices=ROLE, default='C')
    nome_completo = models.CharField(max_length=100, blank= False)
    nascimento    = models.DateField(blank= False)
    cpf           = models.CharField(max_length= 11, blank= False, unique= True)
    telefone      = models.TextField(max_length= 14, blank= False) 
    cep           = models.TextField(max_length= 10, blank= False)
    endereco      = models.TextField( blank= False)
    email         = models.EmailField(unique=True, blank= False)
    #senha         = models.fielddesenha(validators=[MinLengthValidator(8)]) ainda falta um maiúsculo e !@.# estudar doc AbstractUser
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'nome_completo', 'nascimento', 'cpf']
        
    def saves(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.nome_completo
    