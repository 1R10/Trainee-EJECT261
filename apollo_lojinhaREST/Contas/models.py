from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.core.validators import MinLengthValidator
from django.contrib.auth.models import Group

#from . import encontraCEP


class ContaPadrao(AbstractUser):
    ROLE = (
        ('L', 'Lojista'),
        ('C', 'Cliente'),
    )
    role          = models.TextField(choices=ROLE, default='C')
    nome_completo = models.CharField(max_length=100, blank= False)
    nascimento    = models.DateField(blank= False)
    cpf           = models.CharField(max_length= 11, blank= False, unique= True)
    telefone      = models.TextField(max_length= 13,  blank= False) 
    cep           = models.TextField(max_length= 9,  blank= False)
    endereco      = models.TextField(blank=True) # utiliza o encontraCEP
    email         = models.EmailField(unique=True, blank= False)
    REQUIRED_FIELDS = [ 'email', 'nome_completo', 'nascimento', 'cpf','role']
        
    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

        if self.role == 'L':
            nome_grupo = 'Lojista'
        else:
            nome_grupo = 'Cliente'
    
        grupo = Group.objects.get(name=nome_grupo)
        self.groups.set([grupo])
        
    def __str__(self):
        return self.nome_completo
    