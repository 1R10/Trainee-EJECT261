from Produtos.serializers import ProdutosSerializer, Produto, VariacaoProdutoSerializer, VariacaoProduto
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from Contas.permissions import PermissionLojista

class ProdutosViewSets(viewsets.ModelViewSet):  
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [PermissionLojista]
        else:
            self.permission_classes = []

        return super().get_permissions()
    
    queryset = Produto.objects.filter(ativoProduto=True).order_by('precoProduto') # antes objects.all
    serializer_class = ProdutosSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nomeProduto', 'precoProduto']
    ordering = ['nomeProduto'] # ordenação padrão
    filterset_fields = ['nomeProduto', 'precoProduto']
    search_fields = ['nomeProduto', 'precoProduto']
    permission_classes = [AllowAny]

class VariacaoProdutoViewSets(viewsets.ModelViewSet):  
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [PermissionLojista]
        else:
            self.permission_classes = []

        return super().get_permissions()
    
    queryset = VariacaoProduto.objects.all().order_by('id')
    serializer_class = VariacaoProdutoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['tamanhoProduto', 'corProduto']
    ordering = ['tamanhoProduto', 'corProduto'] # ordenação padrão
    filterset_fields = ['tamanhoProduto', 'corProduto']
    search_fields = ['tamanhoProduto', 'corProduto']
    permission_classes = [AllowAny]
    
    