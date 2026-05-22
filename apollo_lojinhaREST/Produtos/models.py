from django.db import models

class Produtos(models.Model):
    nomeProduto      = models.CharField(max_length=200, blank= False)
    descricaoProduto = models.TextField()
    precoProduto     = models.FloatField(blank=False)
    TAMANHOPRODUTO   = (
        ('2p', 'PP'),
        ('p' , 'P'),
        ('m' , 'M'),
        ('g' , 'G'),
        ('2g', 'GG'),
    )  
    tamanhoProduto   = models.TextField(choices=TAMANHOPRODUTO, blank= False) 
    corProduto       = models.TextField(blank= False) # input? tem quantidade de cor por produto e cores infinitas...

    def __str__(self):
        return self.nomeProduto