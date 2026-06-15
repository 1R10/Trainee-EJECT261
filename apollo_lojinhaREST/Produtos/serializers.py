from rest_framework import serializers
from Produtos.models import Produto, VariacaoProduto
from Produtos.validators import nomeProduto_valido, precoProduto_valido, corProduto_valido

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Produto
        fields = '__all__'
    def validate(self, dados):
        if not nomeProduto_valido(dados['nomeProduto']):
            raise serializers.ValidationError({'nomeProduto': 'O nome só pode conter letras.'})
        if not precoProduto_valido(dados['precoProduto']):
            raise serializers.ValidationError({'precoProduto': 'Preço precisa ser positivo'})
                
        return dados

class VariacaoProdutoSerializer(serializers.ModelSerializer):
    nomeProduto = serializers.ReadOnlyField(source='produto.nomeProduto')
    class Meta: 
        model = VariacaoProduto
        fields = '__all__'
    def validate(self, dados):
        variacao = VariacaoProduto.objects.filter(
            produto = dados['produto'],
            corProduto = dados['corProduto'],
            tamanhoProduto = dados['tamanhoProduto']
        )
        if self.instance:
            variacao = variacao.exclude(pk=self.instance.pk) # olha pra si e apaga pra ñ gerar duplicidade.
        if variacao.exists():
            raise serializers.ValidationError({'Cadastro duplo': 'Variação já cadastrada previamente.'})


        if not corProduto_valido(dados['corProduto']):
            raise serializers.ValidationError({'corProduto': 'Não pode conter caracteres especiais.'})
        
        return dados