import re

def cpf_valido (cpf : str):
    if type(cpf) != str:

        return False
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf.isdecimal() == False:

        return False
    if len(cpf) != 11:

        return False
    
    soma = 0
    for pos in range (9):
        soma += int(cpf[pos]) * (10 - pos)
    dv1 = 11 - soma % 11
    if dv1 >= 10: dv1 = 0
        
    if dv1 != int(cpf[9]):

        return False
    
    soma = 0
    for pos in range (10):
        soma += int(cpf[pos]) * (11 - pos)
    dv2 = 11 - soma % 11
    if dv2 >= 10: dv2 = 0
        
    if dv2 != int(cpf[10]):

        return False
    
    return True

def telefone_valido(telefone):
    numero = '[0-9]{2} [9]{1}[0-9]{4}-[0-9]{4}'
    resposta = re.findall(numero,telefone)
    return resposta

def cep_valido(cep):
    numero = '[0-9]{5}-[0-9]{3}'
    resposta = re.findall(numero,cep)
    return resposta

def nome_valido(nome_completo:str):
    if not (nome_completo.replace(' ', '')).isalpha():
        return False
    return True