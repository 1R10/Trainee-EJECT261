import requests
def buscar_endereco(cep):
    endereco_completo = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()

    return f'{endereco_completo["logradouro"]}, {endereco_completo["bairro"]}, {endereco_completo["localidade"]}, {endereco_completo["estado"]}' 