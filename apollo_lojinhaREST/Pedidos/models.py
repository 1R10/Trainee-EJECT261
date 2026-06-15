from django.db import models
from Carrinho.models import Carrinho

class PedidoModel(models.Model):
    STATUS = (
        ('Pend', 'Pendente'),
        ('Apro', 'Aprovado'),
        ('Canc', 'Cancelado')
    )
    PAGAMENTO = (
        ('picx', 'Pix'),
        ('cred', 'Crédito'),
        ('debt', 'Débito')
    )
    
    dataPedido      = models.DateField(auto_now_add=True, verbose_name='Data de abertura')
    statusPedido    = models.TextField(choices=STATUS, blank=False, verbose_name='Status')
    pagamentoPedido = models.TextField(choices=PAGAMENTO, blank=False, verbose_name='Forma de pagamento')
    carrinho        = models.ForeignKey(Carrinho, on_delete=models.CASCADE, verbose_name='Carrinho')

    def valorPedido(self):
        itens = self.carrinho.itemcarrinho_set.all()
        total = 0
        for item in itens:
            total += item.variacao.produto.precoProduto * item.quantidade
        return total
    

def __str__(self):
    recibo = f'''
    Data:      {self.dataPedido}
    Cliente:   {self.carrinho.usuario.nome_completo}
    Pagamento: {self.pagamentoPedido}
    Valor:     R${self.valorPedido()}
    Status:    {self.statusPedido}
    '''
    print(recibo)
    return recibo
    

