from django.db import models

class Produtos(models.Model):
    nomeProduto      = models.CharField(max_length=200, blank= False, verbose_name='Nome')
    descricaoProduto = models.TextField(verbose_name='Descrição')
    precoProduto     = models.FloatField(blank=False, verbose_name='Preço')
    TAMANHOPRODUTO   = (
        ('2p', 'PP'),
        ('p' , 'P'),
        ('m' , 'M'),
        ('g' , 'G'),
        ('2g', 'GG'),
    )  
    tamanhoProduto    = models.TextField(choices=TAMANHOPRODUTO, blank= False, verbose_name='Tamanho') 
    corProduto        = models.TextField(blank= False, verbose_name='Cor')
    estoqueProduto = models.PositiveIntegerField(default=0, verbose_name='Estoque')

    def __str__(self):
        return self.nomeProduto