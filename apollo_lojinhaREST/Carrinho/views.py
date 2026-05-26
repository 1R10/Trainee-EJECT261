from .serializers import (
    CarrinhoSerializer, Carrinho, ItemCarrinho, ItemCarrinhoSerializer, 
    ListaCarrinhoPorContaSerializer, ListaItemPorCarrinhoSerializer)
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CarrinhoViewSets(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes     = [IsAuthenticated] 

    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    
class ItemCarrinhoViewSets(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes     = [IsAuthenticated] 

    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer

class ListaCarrinhoPorContaViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_queryset(self):
        queryset = Carrinho.objects.filter(usuario_id=self.kwargs['pkcontas']) # primary key
        return queryset
    serializer_class = ListaCarrinhoPorContaSerializer

class ListaItemPorCarrinhoViewSet(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_queryset(self):
        queryset = ItemCarrinho.objects.filter(carrinho_id=self.kwargs['pkcarrinhos']) # n podem existir 2 pk's na mesma url
        return queryset
    serializer_class = ListaItemPorCarrinhoSerializer