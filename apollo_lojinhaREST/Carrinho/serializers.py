from rest_framework import serializers
from .models import Carrinho, ItemCarrinho

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = Carrinho
        fields = '__all__'

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ItemCarrinho
        exclude = []

class ListaCarrinhoPorContaSerializer(serializers.ModelSerializer):
    carrinhoData = serializers.ReadOnlyField(source='Carrinho.carrinhoData')
    estado       = serializers.SerializerMethodField()

    class Meta:
        model  = Carrinho
        fields = ['estado', 'carrinhoData']

    def get_estado(self, obj):
        return obj.get_estado_display()
    
    
class ListaItemPorCarrinhoSerializer(serializers.ModelSerializer):
    produtoNome       = serializers.ReadOnlyField(source='Produto.nome')
    produtoQuantidade = serializers.ReadOnlyField(source='ItemCarrinho.quantidade')
    
    class Meta:
        model = ItemCarrinho
        fields = ['produtoNome', 'produtoQuantidade']