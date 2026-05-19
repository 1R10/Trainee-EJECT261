from django.http import JsonResponse
def Contas(request):
    produto = {
        'id': '0',
        'nomeProduto': 'Foguete',
        'nascimento':    'dd/mm/aaaa',
        'cpf':           '12345678910',
        'email':         'tengotelengo@tengoede.carrapixo',
        'senha':         'segredoveinaoexplana',
        'cep':           '0000000000',
        'endereco':      ['rua', 'numero','bairro','cidade','estado','pais','continente'] # isso ta ok?
    }
    return JsonResponse(conta)

