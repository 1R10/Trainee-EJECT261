from .serializers import CarrinhoSerializer, Carrinho
from rest_framework import viewsets

class CarrinhoViewSets(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer