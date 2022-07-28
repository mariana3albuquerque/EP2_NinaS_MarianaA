#importando bibliotecas necessarias:
import time
from base_de_questoes import quest
from gera_ajuda_em_uma_questao import gera_ajuda
from questao_para_texto import questao_para_texto
from sorteia_questao_inedita import sorteia_questao_inedida
#from sorteia_uma_questao import sorteia_questao
from transforma_base import transforma_base
#from valida_questao import valida_questao
from valida_questoes import valida_questoes



#preparando dados para o jogo
lista_falhas = valida_questoes(quest)
if len(lista_falhas) != lista_falhas.count({}):
    print('base esta uma bosta')
    quit()

dicionario_questoes = transforma_base(quest)
acaba = False

while acaba == False:
    #comecando o jogo
    premio = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
    lista_opcoes = ['A',"B","C","D","AJUDA","PULA","PARAR"]
    n = 0
    pulo = 3
    ajuda = 2

    

    print('\n\033[35mOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\033[m\n')
    time.sleep(1)
    nome = input('Qual seu nome? ')

    print(f'\nOk \033[34m{nome.upper()}\033[m, você tem direito a pular 3 vezes e 2 ajudas!\n')
    print('As opções de resposta são \033[36m"A"\033[m, \033[32m"B"\033[m, \033[35m"C"\033[m, \033[34m"D"\033[m, \033[33m"ajuda"\033[m, \033[35m"pula"\033[m e \033[31m"parar"\033[m!\n ')
    time.sleep(1)
    print('O jogo já vai começar! Lá vem a primeira questão!\n')
    time.sleep(1)
    print('Vamos começar com questões do nível \033[32mFACIL\033[m!\n')

    jogadas = 1
    sorteadas = [] #lista de questoes que ja foram
    lista_questoes_usadas = []
    validade = 0
    questao = sorteia_questao_inedida(dicionario_questoes,'facil',sorteadas)
    while acaba == False:
        if  jogadas < 4:
            nivel = 'facil'
        elif jogadas < 7:
            nivel = 'medio'
            if jogadas == 4:
                print ('\nVamos passar para o nível \033[33mMÉDIO\033[m!')
        else:
            nivel = 'dificil'
            if jogadas == 7:
                print('\nAgora você está no nível \033[31mDIFÍIL\033[m!')
            

        #questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
        enunciado = questao_para_texto(questao,jogadas)   #problema quando vai pro nivel medio 
        print(enunciado)
        palpite = input('RESPOSTA: ')

        while palpite.upper() not in lista_opcoes:
            time.sleep(2)
            print("\nOpcão \033[31mInválida\033[m! Tente novamente...\n")
            time.sleep(1)
            print('As opções de resposta são \033[36m"A"\033[m, \033[32m"B"\033[m, \033[35m"C"\033[m, \033[34m"D"\033[m, \033[33m"ajuda"\033[m, \033[35m"pula"\033[m e \033[31m"parar"\033[m!\n ')
            time.sleep(1)
            print(enunciado)
            palpite = input('RESPOSTA: \n')
            validade = 1
        
        if palpite.upper() in lista_opcoes:
                
            if palpite.upper() == 'AJUDA':
                ajuda -=1
                time.sleep(2)
                if ajuda == 0: 
                    print('\nVocê não tem mais \033[33majudas\033[m!, escolha outra opção...\n')
            
                elif ajuda > 0:
                    questao_com_ajuda = gera_ajuda(questao)
                    print('\nOk, lá vem a \033[33majuda\033[m! Você ainda tem \033[33m{} ajudas\033[m\n'.format(ajuda))
                    time.sleep(2)
                    print(questao_com_ajuda)
                    
                '''if palpite.upper() == 'PULA':
                    pulo -=1
                    questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
                    enunciado = questao_para_texto(questao,jogadas)
                    print(enunciado)
                    palpite = input('RESPOSTA: ')
                
                if palpite.upper() == 'AJUDA':
                    time.sleep(2)
                    print('Não deu! Você já pediu uma \033[33majuda\033[m nesta questão!')
                    time.sleep(2)
                    print(enunciado)
                    palpite = input('RESPOSTA: ')'''
                
            if palpite.upper() == 'PARAR':
                time.sleep(2)
                print(f'\nOK! Você vai sair com um prêmio de \033[32m{premio[n]}\033[m REAIS')
                acaba = True
                

            if palpite.upper() == 'PULA':
                pulo -=1
                #questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
                #enunciado = questao_para_texto(questao,jogadas)
                #print(enunciado)
                #palpite = input('RESPOSTA: ')
                if pulo < 0:
                    time.sleep(2)
                    print('\nVocê não tem mais \033[35mpulos\033[m! Escolha outra opção...')
                    #print(enunciado)
                    #palpite = input('RESPOSTA: ')
                    #print('')
                else:
                    print('\nOk, pulando! Você ainda tem \033[35m{} pulos\033[m'.format(pulo))
                    time.sleep(2)
                    questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
                print('')
                
            if palpite.upper() == questao['correta']:
                if n<8:
                    #lista_questoes_usadas.append(questao)
                    n += 1
                    jogadas += 1
                    time.sleep(2)
                    print(f'\n\033[32mParabens\033[m, você acertou! Seu premio agora é de \033[32m{premio[n]}\033[m REAIS\n')
                    time.sleep(1.5)
                    validade = 0
                    questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
                else:
                    time.sleep(2)
                    print ('\033[0,32mPARABÉNS! VOCÊ GANHOU 1 MILHÃO DE REIAS!\033[m')
                    acaba = True 

            elif palpite.upper() != questao['correta'] and palpite.upper()!='PARAR' and palpite.upper()!= 'AJUDA' and palpite.upper()!='PULA':
                time.sleep(2)
                print('\n\033[31mRESPOSTA INCORRETA\033[m! Seu prêmio voltou a ser \033[33m0\033[m REAIS\n ')
                acaba = True
            

    jogar_de_novo = input('\nPressione \033[36mENTER\033[m para reiniciar o jogo')
    if jogar_de_novo == '':
        acaba = False

        











