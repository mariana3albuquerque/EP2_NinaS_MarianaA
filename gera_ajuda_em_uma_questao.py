import random
def gera_ajuda(questao):
    resposta_correta = questao['correta']
    resposta_errada = []
    for chave, resposta in questao['opcoes'].items():
        if chave != resposta_correta:
            resposta_errada.append(resposta)

    qunatas = random.randint(1,3)
    if qunatas == 2:
        sorteio = random.sample(resposta_errada,2)

    else:
        sorteio = random.choices(resposta_errada)

    r = 'DICA:\n'
    r+='Opções certamente erradas: {}'.format(sorteio)
    return r