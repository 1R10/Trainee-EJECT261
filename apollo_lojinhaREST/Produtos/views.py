from Produtos.serializers import ProdutosSerializer,Produtos, VariacaoProdutoSerializer, VariacaoProduto
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
class ProdutosViewSets(viewsets.ModelViewSet):  
    queryset = Produtos.objects.all().order_by('precoProduto')
    serializer_class = ProdutosSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['nomeProduto', 'precoProduto']
    ordering = ['nomeProduto'] # ordenação padrão

class VariacaoProdutoViewSets(viewsets.ModelViewSet):  
    queryset = VariacaoProduto.objects.all().order_by('id')
    serializer_class = VariacaoProdutoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['produto', 'estoqueProduto']
    search_fields   = ['produto']
    ordering = ['produto'] # ordenação padrão
    