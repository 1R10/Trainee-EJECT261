'''
Validators para o carrinho
'''

def estado_validator(estado:str):
    if estado == 'C' or estado == 'F':
        return False
    return True
    

def variacaoNoEstoque_validator(variacao):
    if variacao['estoqueProduto'] < 1: # talvez tenha errado o dict
        return False
    return True

def quantidade_validator(quantidade: int):
    if quantidade < 1:
        return False
    return True