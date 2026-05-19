from rest_framework import serializers
from Produtos.models import Produtos

class ProdutosSerializer(serializers.ModelSerializer):
    class meta: 
        model = Produtos
        fields = '__all__'