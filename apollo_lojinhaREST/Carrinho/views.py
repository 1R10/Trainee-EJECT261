from .serializers import CarrinhoSerializer, Carrinho, ItemCarrinho, ItemCarrinhoSerializer
from rest_framework import viewsets

class CarrinhoViewSets(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    
class ItemCarrinhoViewSets(viewsets.ModelViewSet):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer