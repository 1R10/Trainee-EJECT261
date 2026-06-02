from Produtos.serializers import ProdutosSerializer,Produtos, VariacaoProdutoSerializer, VariacaoProduto
from rest_framework import viewsets

class ProdutosViewSets(viewsets.ModelViewSet):  
    queryset = Produtos.objects.all().order_by('precoProduto')
    serializer_class = ProdutosSerializer

class VariacaoProdutoViewSets(viewsets.ModelViewSet):  
    queryset = VariacaoProduto.objects.all().order_by('id')
    serializer_class = VariacaoProdutoSerializer