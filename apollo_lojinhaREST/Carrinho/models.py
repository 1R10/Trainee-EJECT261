from django.db import models
from Contas.models import ContaPadrao
from Produtos.models import Produtos
class Carrinho(models.Model):
    ESTADO = (
        ('A', 'Aberto'),   # Carrinho atual
        ('F', 'Fechado'),  # Histórico de compras
        ('C', 'Cancelado') # Cancelado vou deletar do banco
    )
    usuario = models.ForeignKey(ContaPadrao, on_delete=models.CASCADE, verbose_name='UsuárioCarrinho') # Usuário deletado, carrinho também.
    estado  = models.CharField(choices=ESTADO, default='A', max_length=1, verbose_name='EstadoCarrinho')
    carrinhoData = models.DateField(auto_now_add=True, verbose_name='InicioCarrinho') # Data de criação do carrinho



    # Optei por fazer os itens a parte. O CASCADE deletaria tudo, então eu preciso de um modelo APENAS para o item do carrinho?
    # Fazer, mas confirmar com Rafa_gamer
    def __str__(self):
        return f'DATA: {self.carrinhoData}, {self.usuario} --> {self.estado}'

class ItemCarrinho(models.Model):
    carrinho   = models.ForeignKey(Carrinho, on_delete=models.CASCADE, verbose_name='ItemCarrinho')
    produto    = models.ForeignKey(Produtos, on_delete=models.CASCADE, verbose_name='ProdutoItemCarrinho')
    quantidade = models.PositiveIntegerField(default=1, verbose_name='QuantidadeItemCarrinho')
    
    def __str__(self):
        return f'{self.produto} x {self.quantidade}'