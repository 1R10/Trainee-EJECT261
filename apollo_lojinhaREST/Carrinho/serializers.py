from rest_framework import serializers
from .models import Carrinho, ItemCarrinho
from Carrinho.validators import estado_validator,variacao_validator, quantidade_validator

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
        exclude = ['produto']

    def validate(self, dados):
        dados['produto'] = dados['variacao'].produto
        if not quantidade_validator(dados['quantidade'], dados['variacao']):
            raise serializers.ValidationError({'quantidade': 'Não temos estoque o suficiente.'})

        return dados
    def create(self, validated_data):
            return ItemCarrinho.objects.create(**validated_data)                

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

        