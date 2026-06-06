import requests
def buscar_endereco(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    for dado in url:
        print(f'{dado}: {url[dado]}')
