from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from Contas.permissions import PermissionCliente, PermissionLojista, PermissionClienteSelf
from Pedidos.models import PedidoModel
from Pedidos.serializers import PedidoSerializer

class PedidosViewsets(viewsets.ModelViewSet):
    def get_permissions(self):
        ''' 
        Apenas Lojistas podem acessar e administrar pedidos. Clientes podem ver
        '''
        if self.request.user == 'GET':
            self.permission_classes = [PermissionClienteSelf, PermissionLojista]
        else:
            self.permission_classes = [PermissionLojista]
        return super().get_permissions()
    
    queryset = PedidoModel.objects.filter().order_by('dataPedido')
    serializer_class = PedidoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['dataPedido','carrinhoData']
    search_fields = ['statusPedido','pagamentoPedido','carrinho', 'dataPedido']
    ordering = ['dataPedido']
    filterset_fields = ['dataPedido', 'statusPedido']

