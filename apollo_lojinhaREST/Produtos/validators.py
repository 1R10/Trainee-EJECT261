# produto base----------------------------------------------------------------
def nomeProduto_valido(nomeProduto:str):
    if not (nomeProduto.replace(' ', '')).isalpha():
        return False
    return True


def descriçãoProduto_valido(descriçãoProduto):
    pass

def precoProduto_valido(precoProduto: float):
    if precoProduto == None:
        return False
    if precoProduto < 0: # Preço pode ser zero sem promoção (?)
        return False
    
    return True

# variação-----------------------------------------------------------------------------

def tamanhoProduto_valido(tamanhoProduto: str):
    pass

def corProduto_valido(corProduto:str):
    if not (corProduto.replace(' ', '').replace(',', '')).isalnum(): # alphanum em caso do front add tabulação de cor com número
        return False
    return True

def estoqueProduto_valido(estoqueProduto: int):
    pass