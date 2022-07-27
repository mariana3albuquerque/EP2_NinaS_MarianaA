#importando bibliotecas necessarias:
import time
from base_de_questoes import quest
from gera_ajuda_em_uma_questao import gera_ajuda
from questao_para_texto import questao_para_texto
from sorteia_questao_inedita import sorteia_questao_inedida
from sorteia_uma_questao import sorteia_questao
from transforma_base import transforma_base
from valida_questao import valida_questao
from valida_questoes import valida_questoes


#preparando dados para o jogo
lista_falhas = valida_questoes(quest)
if len(lista_falhas) != lista_falhas.count({}):
    print('base esta uma bosta')
    quit()

dicionario_questoes = transforma_base(quest)




#comecando o jogo
premio = 0
pulo = 3
ajuda = 2

acaba = False

print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
time.sleep(2)
print('')
print('')
nome = input('Qual seu nome?')

print(f'Ok {nome.upper()}, você tem direito a pular 3 vezes e 2 ajudas!')
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"! ')
time.sleep(5)
print('')
print('O jogo já vai começar! Lá vem a primeira questão!')
print(" \n  ")
time.sleep(3)
print('Vamos começar com questões do nível FACIL!')

jogadas = 1
sorteadas = [] #lista de questoes que ja foram
while acaba == False:
    while jogadas < 4:
        questao = sorteia_questao_inedida(dicionario_questoes,'facil',sorteadas)
        enunciado = questao_para_texto(questao,jogadas)
        print(enunciado)
        palpite = input('RESPOSTA: ')
        if palpite == 'ajuda':
            time.sleep(2)
            questao_com_ajuda = gera_ajuda(questao)
            print(questao_com_ajuda)
            palpite = input('RESPOSTA: ')
            
        if palpite.upper() == questao['correta']:
            premio = 1000
            jogadas += 1
            print(f'Parabens, voce acertou\n seu premio agora é de {premio} CONTOS DE REIS ')
        else:
            print('PERDEU. VAI SAIR SEM NADA TROXA')
            acaba = True

jogar_de_novo = input('pressione ENTER para jogar de novo')
if jogar_de_novo == '':
    acaba = False
    











