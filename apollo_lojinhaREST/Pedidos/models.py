from django.db import models
from Carrinho.models import  ItemCarrinho

# itemcarrinho possui TUDO. produto, variacao, user, carrinho... TUDO
class PedidoModel(models.Model):
    '''
    Classe do objeto de pedido.
    Vai receber os itens de um carrinho junto de seus atributos.
    Vai calcular o valor do pedido e aprovar/cancelar pagamento.
    '''
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
    itensPedido     = models.ForeignKey(ItemCarrinho, on_delete=models.CASCADE, blank=False, verbose_name='Itens')
 
        
    

    def __str__(self):
        recibo = f'''
        Data:     {self.dataPedido}
        Cliente: {self.itensPedido.carrinho.usuario.nome_completo}
        Pagamento: {self.pagamentoPedido}
        Valor: R${self.valorPedido}
        Status: {self.statusPedido}
        itens: {self.itensPedido.variacao}
                '''
        print(recibo)
        return recibo
    

