from .serializers import (
    CarrinhoSerializer, Carrinho, ItemCarrinho, ItemCarrinhoSerializer, 
    ListaCarrinhoPorContaSerializer, ListaItemPorCarrinhoSerializer)
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class CarrinhoViewSets(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all().order_by('id')
    serializer_class = CarrinhoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['estado','carrinhoData']
    search_fields = ['carrinhoData']
    ordering = ['carrinhoData']
    
    
class ItemCarrinhoViewSets(viewsets.ModelViewSet): # nao precisa de filtro de paginacao
    queryset = ItemCarrinho.objects.all().order_by('id')
    serializer_class = ItemCarrinhoSerializer

class ListaCarrinhoPorContaViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Carrinho.objects.filter(dono_id=self.kwargs['pkcontas']).order_by('id') # primary key
        return queryset
    serializer_class = ListaCarrinhoPorContaSerializer

class ListaItemPorCarrinhoViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = ItemCarrinho.objects.filter(carrinho_id=self.kwargs['pkcarrinhos']).order_by('id') # n podem existir 2 pk's na mesma url
        return queryset
    serializer_class = ListaItemPorCarrinhoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['produto', 'quantidade']
    ordering = ['produto']