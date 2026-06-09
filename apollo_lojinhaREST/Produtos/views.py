from Produtos.serializers import ProdutosSerializer, Produto, VariacaoProdutoSerializer, VariacaoProduto
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from Contas.permissions import PermissionLojista

class ProdutosViewSets(viewsets.ModelViewSet):  
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [PermissionLojista]
        else:
            self.permission_classes = []

        return super().get_permissions()
    
    queryset = Produto.objects.all().order_by('precoProduto').order_by('id')
    serializer_class = ProdutosSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['nomeProduto', 'precoProduto']
    ordering = ['nomeProduto'] # ordenação padrão

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
    ordering_fields = ['produto', 'estoqueProduto']
    search_fields   = ['produto']
    ordering = ['produto'] # ordenação padrão
    