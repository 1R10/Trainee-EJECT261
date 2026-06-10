from django.db import models
from Carrinho.models import  ItemCarrinho

# itemcarrinho possui TUDO. produto, variacao, user, carrinho... TUDO
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
    
    statusPedido    = models.TextField(choices=STATUS, blank=False)
    pagamentoPedido = models.TextField(choices=PAGAMENTO, blank=False)
    itensPedido     = models.ForeignKey(ItemCarrinho, on_delete=models.CASCADE, blank=False)
    

