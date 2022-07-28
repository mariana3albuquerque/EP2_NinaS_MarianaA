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
premio = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
lista_opcoes = ['A',"B","C","D","AJUDA","PULA","PARAR"]
n = 0
pulo = 3
ajuda = 2

acaba = False

print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
time.sleep(1)
print('')
print('')
nome = input('Qual seu nome? ')

print(f'Ok {nome.upper()}, você tem direito a pular 3 vezes e 2 ajudas!')
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"! ')
time.sleep(1)
print('')
print('O jogo já vai começar! Lá vem a primeira questão!')
print(" \n  ")
time.sleep(1)
print('Vamos começar com questões do nível FACIL!')

jogadas = 1
sorteadas = [] #lista de questoes que ja foram
lista_questoes_usadas = []
validade = 0

while acaba == False:
    if  jogadas < 4:
        nivel = 'facil'
    elif jogadas < 7:
        print ('Vamos passar para o nível MEDIO!')
        nivel = 'medio'
    else:
        print('Agora você está no nível DIFIIL!')
        nivel = 'dificil'

    questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
    enunciado = questao_para_texto(questao,jogadas)   #problema quando vai pro nivel medio 


    if questao in lista_questoes_usadas and validade == 0:
        questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
        enunciado = questao_para_texto(questao,jogadas)

    elif questao not in lista_questoes_usadas:
        print(enunciado)
        palpite = input('RESPOSTA: ')
        print('')

        if palpite.upper() not in lista_opcoes:
            print("Opcão Inválida!")
            print(enunciado)
            palpite = input('RESPOSTA: ')
            print('')
            validade = 1
        
        if palpite.upper() in lista_opcoes:
                
            if palpite.upper() == 'AJUDA':
                ajuda -=1
                time.sleep(2)
                if ajuda == 0: 
                    print('Você não tem mais ajudas!, escolha outra opção...')
                    print('')
                    print(enunciado)
                    palpite = input('RESPOSTA: ')
                    print('')
                elif ajuda > 0:
                    questao_com_ajuda = gera_ajuda(questao)
                    print('Ok, lá vem a ajuda! Você ainda tem {} ajudas'.format(ajuda))
                    time.sleep(2)
                    print(questao_com_ajuda)
                    print('')
                    time.sleep(2)
                    print(enunciado)
                    palpite = input('RESPOSTA: ')
                    print('')
                
                if palpite.upper() == 'PULA':
                    pulo -=1
                    questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
                    enunciado = questao_para_texto(questao,jogadas)
                    print(enunciado)
                    palpite = input('RESPOSTA: ')
                
                if palpite.upper() == 'AJUDA':
                    print('Não deu! Você já pediu uma ajuda nesta questão!')
                    time.sleep(2)
                    print(enunciado)
                
                if palpite.upper() == 'PARAR':
                    print(f'PARABÉNS! Você vai sair com um prêmio de {premio[n]} CONTOS DE REIS')
                    acaba = True
                

            if palpite.upper() == 'PULA':
                pulo -=1
                questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
                enunciado = questao_para_texto(questao,jogadas)
                print(enunciado)
                palpite = input('RESPOSTA: ')
                if pulo == 0:
                    print('Você não tem mais pulos!, escolha outra opção...')
                    print(enunciado)
                    palpite = input('RESPOSTA: ')
                    print('')
                else:
                    print('Ok, pulando! Você ainda tem {} pulos'.format(pulo))
                print('')
                
            if palpite.upper() == questao['correta']:
                lista_questoes_usadas.append(questao)
                n += 1
                jogadas += 1
                print(f'Parabens, voce acertou! Seu premio agora é de {premio[n]} CONTOS DE REIS ')
                validade = 0
            else:
                print('PERDEU. VAI SAIR SEM NADA TROXA')
                acaba = True

jogar_de_novo = input('pressione ENTER para jogar de novo')
if jogar_de_novo == '':
    acaba = False
    











