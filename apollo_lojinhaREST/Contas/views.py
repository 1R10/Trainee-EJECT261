from Contas.serializers import ContaPadraoSerializer, ContaPadrao
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ContaPadraoViewSets(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes     = [IsAuthenticated]   
    
    queryset = ContaPadrao.objects.all()
    serializer_class = ContaPadraoSerializer



''' salvando para revisitar depois caso necessário!

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