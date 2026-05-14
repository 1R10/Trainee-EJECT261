from django.http import JsonResponse
# Aqui gero os meus http's. Perguntar o motivo de não usar o https já que https>http. Concluir a trilha antes para sanar a dúvida nela se possível
# Lembrar de enviar pras URL's na pasta mãe
def Contas(request):
    conta = {
        'id': '0',
        'nome_completo': 'nome',
        'nascimento':    'dd/mm/aaaa',
        'cpf':           '12345678910',
        'email':         'tengotelengo@tengoede.carrapixo',
        'senha':         'segredoveinaoexplana',
        'cep':           '0000000000',
        'endereco':      ['rua', 'numero','bairro','cidade','estado','pais','continente'] # isso ta ok?
    }
    return JsonResponse(conta)

