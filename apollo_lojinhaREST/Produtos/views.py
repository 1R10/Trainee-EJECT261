from Produtos.serializers import ProdutosSerializer,Produtos, VariacaoProdutoSerializer, VariacaoProduto
from rest_framework import viewsets

class ProdutosViewSets(viewsets.ModelViewSet):  
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

class VariacaoProdutoViewSets(viewsets.ModelViewSet):  
    queryset = VariacaoProduto.objects.all()
    serializer_class = VariacaoProdutoSerializer