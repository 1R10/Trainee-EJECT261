from rest_framework import serializers
from Produtos.models import Produtos, VariacaoProduto

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Produtos
        fields = '__all__'

class VariacaoProdutoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = VariacaoProduto
        fields = '__all__'