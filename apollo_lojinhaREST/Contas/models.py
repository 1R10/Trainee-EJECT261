from django.db import models

class Cadastrar_user(models.Model):
    ROLE = (
        ('L', 'Lojista'),
        ('C', 'Cliente'),
    )
    role          = models.TextField(choices=ROLE, default='C')
    nome_completo = models.CharField(max_length=100, blank= False)
    nascimento    = models.DateField(blank= False)
    cpf           = models.CharField(max_length= 11, blank= False)
    email         = models.EmailField(max_length= 100, blank= False)
    senha         = models.TextField(max_length= 50, blank= False) # min 8 car, 1 maiuscula 1 especial
    telefone      = models.TextField(max_length= 14, blank= False) 
    cep           = models.TextField(max_length= 10, blank= False)
    endereco      = models.TextField( blank= False)

    def __str__(self):
        return self.nome_completo

class Cadastrar_produto(models.Model):
    nome_produto      = models.CharField(max_length=200)
    preco_produto     = models.FloatField() 

    COR_PRODUTO = (
        ('')
    )
    tamanho_produto   = models.TextField() 
    cor_produto       = models.TextField() # input? tem quantidade de cor por produto e cores infinitas...
    descricao_produto = models.TextField()

    def __str__(self):
        return self.nome_produto