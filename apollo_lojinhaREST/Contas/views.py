from django.http import JsonResponse
# Aqui gero os meus http's. Perguntar o motivo de não usar o https já que https>http. Concluir a trilha antes para sanar a dúvida nela se possível
# Lembrar de enviar pras URL's na pasta mãe
def Contas(request):
    conta = {
        'id': '1',
        'nome': 'Ryan'
    }
    return JsonResponse(Contas)