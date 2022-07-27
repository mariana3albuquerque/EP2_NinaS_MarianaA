

def valida_questoes(lista):
    from valida_questao import valida_questao
    nl = []
    for i in range(len(lista)):
        erros = valida_questao(lista[i])
        nl.append(erros)
    return nl
