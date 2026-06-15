from .serializers import (
    CarrinhoSerializer, Carrinho, ItemCarrinho, ItemCarrinhoSerializer, 
    ListaCarrinhoPorContaSerializer, ListaItemPorCarrinhoSerializer)
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from Contas.permissions import PermissionCliente, PermissionLojista, PermissionClienteSelf


class CarrinhoViewSets(viewsets.ModelViewSet):
    def get_permissions(self):
        ''' 
        Permissões de Carrinho:
        Lojista: get
        Cliente: get, post, put, patch, delete
        Qualquer um: apenas logado.
        '''
        if self.request.method in ['GET']:
            self.permission_classes = [PermissionClienteSelf, PermissionLojista]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [PermissionClienteSelf]
        return super().get_permissions()



    queryset = Carrinho.objects.all().order_by('id')
    serializer_class = CarrinhoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['estado','carrinhoData']
    search_fields = ['carrinhoData']
    ordering = ['carrinhoData']
    filterset_fields = ['estado', 'carrinhoData']
    
    
    
class ItemCarrinhoViewSets(viewsets.ModelViewSet): # nao precisa de filtro de paginacao
    def get_permissions(self):
        '''
        Permissões de Item por carrinho
        Lojista: delete
        Cliente: post, put, patch, delete
        Qualquer um: get
        '''
    
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            self.permission_classes = [PermissionCliente]
        elif self.request.method == 'DELETE':
            self.permission_classes = [PermissionCliente, PermissionLojista]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
        
    queryset = ItemCarrinho.objects.all().order_by('variacao')
    serializer_class = ItemCarrinhoSerializer

class ListaCarrinhoPorContaViewSet(generics.ListAPIView):
    def get_permissions(self):
        '''
        Permissões de Carrinho por Conta:
        Lojista: get 
        Cliente: get - conta dele
        Qualquer um: nenhuma permissão
        '''
        if self.request.method == 'get':
            self.permission_classes = [PermissionClienteSelf, PermissionLojista]

        return super().get_permissions()

    def get_queryset(self):
        queryset = Carrinho.objects.filter(usuario_id=self.kwargs['pkcontas']).order_by('id') # primary key
        return queryset
    serializer_class = ListaCarrinhoPorContaSerializer

class ListaItemPorCarrinhoViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = ItemCarrinho.objects.filter(carrinho_id=self.kwargs['pkcarrinhos']).order_by('id') # n podem existir 2 pk's na mesma url
        return queryset
    serializer_class = ListaItemPorCarrinhoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['produto', 'quantidade']
    ordering = ['produto']