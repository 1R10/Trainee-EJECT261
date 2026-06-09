from rest_framework import serializers
from .models import Carrinho, ItemCarrinho
from Carrinho.validators import estado_validator,variacaoNoEstoque_validator, quantidade_validator

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = Carrinho
        fields = '__all__'
        def validate(self, dados):
            if not estado_validator(dados['estado']):
                raise serializers.ValidationError({'estado':'Não pode adicionar produtos em carrinhos fechados.'})
            return dados
class ItemCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ItemCarrinho
        fields = '__all__'
    def validate(self, dados):
        if not variacaoNoEstoque_validator(dados['quantidade']):
            raise serializers.ValidationError({'quantidade': 'Sinto muito. Este produto não está em estoque.'})
        if not quantidade_validator(dados['quantidade']):
            raise serializers.ValidationError({'quantidade': 'Coloque no mínimo 1 produto.'})
        return dados
            

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