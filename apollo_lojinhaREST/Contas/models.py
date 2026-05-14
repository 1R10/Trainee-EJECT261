from django.db import models

class Cadastrar_user(models.Model):
    nome_completo = models.CharField(max_length=100, blank= False)
    nascimento    = models.DateField(blank= False)
    cpf           = models.CharField(max_length=11, blank= False)
    email         = models.EmailField(max_length=100, blank= False)
    senha         = models.TextField(max_length=50, blank= False) # min 8 car, 1 maiuscula 1 especial
    telefone      = models.TextField(max_length=14, blank= False) 
    cep           = models.TextField(max_length=10, blank= False)
    endereco      = models.TextField( blank= False)

def __str__(self):
    return self.nome_completo