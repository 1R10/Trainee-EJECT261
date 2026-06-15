from Contas.serializers import ContaPadraoSerializer, ContaPadrao
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from Contas.permissions import PermissionLojista, PermissionCliente, PermissionClienteSelf

class ContaPadraoViewSets(viewsets.ModelViewSet):
    '''
    Recebe permissões de acesso das contas.
    Filtra por nome completo ou role (Lojista/CLiente)

    '''
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [PermissionClienteSelf]
        elif self.request.method in ['PUT', 'PATCH']:
            self.permission_classes = [PermissionClienteSelf]
        elif self.request.method == 'POST':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
  
    queryset = ContaPadrao.objects.all().order_by('id')
    serializer_class = ContaPadraoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome_completo', 'id']
    search_fields   = ['nome_completo', 'cpf']
    ordering = ['nome_completo'] # ordenação padrão
    filterset_fields = ['role', 'nome_completo']
    permission_classes = [AllowAny]



''' salvando para revisitar depois caso necessário!
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated # auth individual
class bla bla bla(viewset.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes     = [IsAuthenticated]

from django.http import JsonResponse
def Contas(request):
    conta = {
        'id':            '0',
        'nome_completo': 'Apollo Foca Artista',
        'nascimento':    'aaaa/mm/dd',
        'cpf':           '12345678910',
        'email':         'inicio@meio.fim',
        'senha':         'Senh@!78',
        'cep':           '1234567890',
        'endereco':      ['rua', 'numero','bairro','cidade','estado','pais','continente'] # isso ta ok?
    }
    return JsonResponse(conta)

'''