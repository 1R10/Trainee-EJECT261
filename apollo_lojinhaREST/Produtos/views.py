from Produtos.serializers import ProdutosSerializer,Produtos
from rest_framework import viewsets

class ProdutosViewSets(viewsets.ModelViewSet):  
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer