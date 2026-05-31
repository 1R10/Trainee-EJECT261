def cpf_valido (cpf : str):
    if type(cpf) != str:
#        print('cpf inválido!')
        return False
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf.isdecimal() == False:
#        print('cpf inválido!')
        return False
    if len(cpf) != 11:
#        print('cpf inválido!')
        return False
    
    soma = 0
    for pos in range (9):
        soma += int(cpf[pos]) * (10 - pos)
    dv1 = 11 - soma % 11
    if dv1 >= 10: dv1 = 0
        
    if dv1 != int(cpf[9]):
#        print('cpf inválido!')
        return False
    
    soma = 0
    for pos in range (10):
        soma += int(cpf[pos]) * (11 - pos)
    dv2 = 11 - soma % 11
    if dv2 >= 10: dv2 = 0
        
    if dv2 != int(cpf[10]):
#        print('cpf inválido!')
        return False
    
    return True
