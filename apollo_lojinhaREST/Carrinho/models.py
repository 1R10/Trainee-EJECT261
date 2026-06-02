from django.db import models
from Contas.models import ContaPadrao
from Produtos.models import Produtos,VariacaoProduto

class Carrinho(models.Model):
    ESTADO = (
        ('A', 'Aberto'),   # Carrinho atual
        ('F', 'Fechado'),  # Histórico de compras
        ('C', 'Cancelado') # Cancelado vou deletar do banco
    )
    usuario      = models.ForeignKey(ContaPadrao, on_delete=models.CASCADE, verbose_name='Dono') # Usuário deletado, carrinho também.
    estado       = models.CharField(choices=ESTADO, default='A', max_length=1, verbose_name='Estado')
    carrinhoData = models.DateField(auto_now_add=True, verbose_name='Abertura')

    def __str__(self):
        return f'{self.usuario} - {self.estado} - {self.id}'

class ItemCarrinho(models.Model):
    carrinho   = models.ForeignKey(Carrinho, on_delete=models.CASCADE, verbose_name='Carrinho')
    produto    = models.ForeignKey(Produtos, on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.PositiveIntegerField(default=1, verbose_name='Quantidade')
    
    def __str__(self):
        return f'{self.produto} x {self.quantidade}'