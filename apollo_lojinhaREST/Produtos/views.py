from Produtos.serializers import ProdutosSerializer,Produtos
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProdutosViewSets(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes     = [IsAuthenticated] 
    
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer