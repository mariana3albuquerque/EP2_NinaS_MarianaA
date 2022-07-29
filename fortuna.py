#importando bibliotecas necessarias:
import time
from base_de_questoes import quest
from gera_ajuda_em_uma_questao import gera_ajuda
from questao_para_texto import questao_para_texto
from sorteia_questao_inedita import sorteia_questao_inedida
from transforma_base import transforma_base
from valida_questoes import valida_questoes



#preparando dados para o jogo
lista_falhas = valida_questoes(quest)
if len(lista_falhas) != lista_falhas.count({}):
    print('base esta com erro')
    quit()

dicionario_questoes = transforma_base(quest)
acaba = False

while acaba == False:  #looping que permite reiniciar o jogo
    #comecando o jogo
    premio = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
    lista_opcoes = ['A',"B","C","D","AJUDA","PULA","PARAR"]
    n = 0  #indice para chamar elemento de premio
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
    sorteadas = [] #lista de questoes que ja foram sorteadas
    questao = sorteia_questao_inedida(dicionario_questoes,'facil',sorteadas)
    ja_pediu_ajuda = False #nao pode pedir ajuda duas vezes na mesma questao
    while acaba == False:
        if  jogadas < 4: #as tres primeiras questoes sao faceis
            nivel = 'facil'
        elif jogadas < 7: #as tres proximas sao medias
            nivel = 'medio'
            if jogadas == 4:
                print ('\nVamos passar para o nível \033[33mMÉDIO\033[m!')
        else:
            nivel = 'dificil' #as ultimas sao dificeis
            if jogadas == 7:
                print('\nAgora você está no nível \033[31mDIFÍIL\033[m!')
            

        enunciado = questao_para_texto(questao,jogadas)   #transformando questao pra texto de acordo com o nivel
        print(enunciado)
        palpite = input('RESPOSTA: ')

        while palpite.upper() not in lista_opcoes:    #looping para resposta invalida
            time.sleep(2)
            print("\nOpcão \033[31mInválida\033[m! Tente novamente...\n")
            time.sleep(1)
            print('As opções de resposta são \033[36m"A"\033[m, \033[32m"B"\033[m, \033[35m"C"\033[m, \033[34m"D"\033[m, \033[33m"ajuda"\033[m, \033[35m"pula"\033[m e \033[31m"parar"\033[m!\n ')
            time.sleep(1)
            print(enunciado)
            palpite = input('RESPOSTA: \n')
            
        
        if palpite.upper() in lista_opcoes:  #resposta valida
                
            if palpite.upper() == 'AJUDA':    #caso peça ajuda
                if ja_pediu_ajuda == True :  #ja pediu ajuda na questao
                    time.sleep(2)
                    print('\nNão deu! Você já pediu uma \033[33majuda\033[m nesta questão!')
                    time.sleep(2)
                    print(enunciado)
                    palpite = input('RESPOSTA: ')
                else: #nao pediu ajuda na questao
                    ja_pediu_ajuda = True
                    ajuda -=1
                    time.sleep(2)
                    if ajuda < 0: #sem ajudas disponiveis
                        print('\nVocê não tem mais \033[33majudas\033[m!, escolha outra opção...\n')
                        time.sleep(2)
                
                    elif ajuda >= 0:  #com ajudas disponiveis
                        questao_com_ajuda = gera_ajuda(questao)
                        print('\nOk, lá vem a \033[33majuda\033[m! Você agora tem \033[33m{} ajudas disponíveis\033[m\n'.format(ajuda))
                        time.sleep(2)
                        print(questao_com_ajuda)
                        time.sleep(2)
                    
            if palpite.upper() == 'PARAR':  #quando o jogador quer parar
                time.sleep(2)
                print(f'\nOK! Você vai sair com um prêmio de \033[32m{premio[n]}\033[m REAIS')
                acaba = True
                

            if palpite.upper() == 'PULA': #quando jogador quer pular
                pulo -=1
                
                if pulo < 0:  #sem pulos disponiveis
                    time.sleep(2)
                    print('\nVocê não tem mais \033[35mpulos\033[m! Escolha outra opção...')
                    
                else: #com pulos disponiveis
                    print('\nOk, pulando! Você agora tem \033[35m{} pulos disponíveis\033[m'.format(pulo))
                    time.sleep(2)
                    questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
                    ja_pediu_ajuda = False
                print('')
                
            if palpite.upper() == questao['correta']:  #acertou a questao
                if n<8: #enquanto nao chegou na pergunta do milhao
                    n += 1
                    jogadas += 1
                    time.sleep(2)
                    print(f'\n\033[32mParabens\033[m, você acertou! Seu premio agora é de \033[32m{premio[n]}\033[m REAIS\n')
                    time.sleep(1.5)
                    questao = sorteia_questao_inedida(dicionario_questoes,nivel,sorteadas)
                    ja_pediu_ajuda = False
                else:     #pergunta do milhao
                    time.sleep(2)
                    print ('\033[1;32mPARABÉNS! VOCÊ GANHOU 1 MILHÃO DE REAIS!\033[m')
                    acaba = True 

            # RESPOSTA ERRADA
            elif palpite.upper() != questao['correta'] and palpite.upper()!='PARAR' and palpite.upper()!= 'AJUDA' and palpite.upper()!='PULA':
                time.sleep(2)
                print('\n\033[31mRESPOSTA INCORRETA\033[m! Você perdeu e vai sair com \033[33m0\033[m REAIS\n ')
                acaba = True
            
    #REINICIANDO O JOGO

    jogar_de_novo = input('\nPressione \033[36mENTER\033[m para reiniciar o jogo')
    if jogar_de_novo == '':
        acaba = False












