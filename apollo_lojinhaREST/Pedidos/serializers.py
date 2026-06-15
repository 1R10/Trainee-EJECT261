from rest_framework import serializers
from Pedidos.models import PedidoModel

class PedidoSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = PedidoModel
        exclude = []

    def validate(self, dados):
        carrinho = dados['carrinho']
        itens = carrinho.itemcarrinho_set.all()

        if len(itens) == 0:
            raise serializers.ValidationError({'carrinho': 'Carrinho está vazio.'})

        for item in itens:
            if item.quantidade > item.variacao.estoqueProduto:
                raise serializers.ValidationError({'estoque': f'{item.variacao.produto.nomeProduto} não tem estoque suficiente.'})
        
        return dados