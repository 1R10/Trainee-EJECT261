from django.db.models.signals import post_save
from Carrinho.models import Carrinho
from Pedidos.models import PedidoModel

def atualizarEstoque(sender, instance, created, **kwargs):
    if instance.estado == 'F': # carrinho fechou, pedido chamou
        itens = instance.itemcarrinho_set.all()
        for item in itens:
            variacao = item.variacao
            variacao.estoqueProduto -= item.quantidade
            variacao.save()

post_save.connect(atualizarEstoque, sender=Carrinho)