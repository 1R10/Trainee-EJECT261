from rest_framework import serializers
from .models import Carrinho, ItemCarrinho

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = Carrinho
        fields = '__all__'

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ItemCarrinho
        fields = '__all__'
        # exclude = []

class ListaCarrinhoPorContaSerializer(serializers.ModelSerializer):
    aberturaCarrinhoData = serializers.ReadOnlyField(source='carrinhoData')
    estado   = serializers.SerializerMethodField()

    class Meta:
        model  = Carrinho
        fields = ['id', 'estado', 'aberturaCarrinhoData']

    def get_estado(self, obj):
        return obj.get_estado_display() # isso aqui usa-se em campos salvos como ('a','aberto')
    
    
class ListaItemPorCarrinhoSerializer(serializers.ModelSerializer):
    produtoNome       = serializers.ReadOnlyField(source='produto.nomeProduto')
    produtoQuantidade = serializers.ReadOnlyField(source='quantidade')
    
    class Meta:
        model = ItemCarrinho
        fields = ['produtoNome', 'produtoQuantidade']