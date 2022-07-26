import random
def sorteia_questao(d_questoes,nivel):
    questoes = d_questoes[nivel]
    questao_sorteada = {}
    if len(questoes) > 0:
        sorteio = random.randint(0,len(questoes)-1)  
        questao_sorteada = questoes[sorteio]
    return questao_sorteada