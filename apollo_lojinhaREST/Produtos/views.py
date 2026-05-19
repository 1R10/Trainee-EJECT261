from django.http import JsonResponse
def Produtos(request):
    produto = {
        'id': '0',
        'nomeProduto':        'Jaqueta Arrasa Foguetes',
        'descricaoProduto':   'Jaqueta de algodão para focas de pelucia',
        'precoProduto':       'R$999.99',
        'tamanhoProduto':     'M',
        'corProduto':         ['Vermelho', 'Preto', 'Azul']
    }
    return JsonResponse(Produtos)

