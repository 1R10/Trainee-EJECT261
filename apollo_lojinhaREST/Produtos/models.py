from django.db import models

class Produto(models.Model):
    '''Aqui será cadastrado o produto'''

    nomeProduto      = models.CharField(max_length=200, blank= False, verbose_name='Nome')
    descricaoProduto = models.TextField(verbose_name='Descrição')
    precoProduto     = models.DecimalField(blank=False,default=0, decimal_places=2,max_digits=999999, verbose_name='Preço')

    def __str__(self):
        return f'{self.nomeProduto}'
    
class VariacaoProduto(models.Model):
    '''Aqui será cadastrada a variação com base em um obj de Produtos'''

    produto           = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto') # provavelmente tem um produto.nomeProduto
    TAMANHOPRODUTO   = (
        ('p' , 'P'),
        ('m' , 'M'),
        ('g' , 'G'),
    )  
    tamanhoProduto     = models.TextField(default='m',choices=TAMANHOPRODUTO, blank= False, verbose_name='Tamanho') 
    corProduto         = models.TextField(blank= False, verbose_name='Cor')
    estoqueProduto = models.PositiveIntegerField(default=0, verbose_name='Estoque') # ver um jeito de associar com produto e somar total

    def __str__(self):
        return f'{self.produto.nomeProduto} - {self.corProduto} - {self.tamanhoProduto} - {self.estoqueProduto}'