import random
def sorteia_questao_inedida(dicionario_questoes, nivel, lista_questoes):
    questoes = dicionario_questoes[nivel]
    questao_sorteada = {}
    if len(questoes) > 0:
        sorteio = random.randint(0,len(questoes)-1)  
        questao_sorteada = questoes[sorteio]
    if questao_sorteada not in lista_questoes:
        lista_questoes.append(questao_sorteada)
        return questao_sorteada