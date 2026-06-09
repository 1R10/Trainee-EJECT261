# carrinho--------------------------------------
def usuario_validator(usuario):
    pass


def estado_validator(estado:str):
    if estado == 'C' or estado == 'F': # carrinho F só pode ser atualizado, não criado.
        return False
    return True


def carrinhoData_validator(carrinhoData):
    pass


# itemCarrinho----------------------------------------------------
def variacao_validator(variacao):
    pass


def quantidade_validator(quantidade: int, variacao):
    print(f"AQUIIIIIIIIIIIIIII --------------------> {variacao.estoqueProduto}")
    if quantidade > variacao.estoqueProduto:
        return False
    return True # lembrar: o estoque não é removido aqui. só no "caixa"