'''
Validators de produtos e suas variações.
'''
def nomeProduto_valido(nomeProduto:str):
    if not (nomeProduto.replace(' ', '')).isalpha():
        return False
    return True

# descriçãoProduto não tem o que fazer.

def precoProduto_valido(precoProduto: float):
    if precoProduto == None:
        return False
    if precoProduto < 0: # Preço pode ser zero sem promoção (?)
        return False
    
    return True

# tamanhoProduto não tem o que fazer.

def corProduto_valido(corProduto:str):
    if not (corProduto.replace(' ', '').replace(',', '')).isalnum(): # alphanum em caso do front add tabulação de cor com número
        return False
    return True

# já validado em models