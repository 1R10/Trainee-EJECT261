from django.db import models

class Produtos(models.Model):
    nomeProduto      = models.CharField(max_length=200)
    descricaoProduto = models.TextField()
    precoProduto     = models.FloatField()
    TAMANHOPRODUTO   = (
        ('PP', 'Minusculo'),
        ('P' , 'Pequeno'),
        ('M' , 'Mediano'),
        ('G' , 'Grande'),
        ('GG', 'Imenso'),
    )  
    tamanhoProduto   = models.TextField(choices=TAMANHOPRODUTO, default='M') 
    corProduto       = models.TextField() # input? tem quantidade de cor por produto e cores infinitas...

    def __str__(self):
        return self.nomeProduto