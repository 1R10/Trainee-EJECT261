from .serializers import CarrinhoSerializer, Carrinho, ItemCarrinho, ItemCarrinhoSerializer, ListaCarrinhoPorContaSerializer, ListaItemPorCarrinhoSerializer
from rest_framework import viewsets, generics

class CarrinhoViewSets(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    
class ItemCarrinhoViewSets(viewsets.ModelViewSet):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer

class ListaCarrinhoPorContaViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Carrinho.objects.filter(usuario_id=self.kwargs['pkcontas']) # primary key
        return queryset
    serializer_class = ListaCarrinhoPorContaSerializer

class ListaItemPorCarrinhoViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = ItemCarrinho.objects.filter(carrinho_id=self.kwargs['pkcarrinhos']) # n podem existir 2 pk's na mesma url
        return queryset
    serializer_class = ListaItemPorCarrinhoSerializer