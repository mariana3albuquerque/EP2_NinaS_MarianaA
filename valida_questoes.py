import valida_questao

def valida_questoes(lista):
    nl = []
    for i in range(len(lista)):
        erros = valida_questao(lista[i])
        nl.append(erros)
    return nl
