questao = {
  'nivel': 'facil'
  }

def valida_questao(questao):
    lista = ['titulo', 'nivel', 'opcoes', 'correta']
    questao_nova = {}
    erro = 0
    #verificando se titulo, nivel, opcoes e correta estao na questao:
    
    for chave in lista:
        
        if chave  not in questao:
            questao_nova[chave] = 'nao_encontrado'
            
    
    #numero de chaves
    if len(questao.keys()) != 4:
        questao_nova['outro'] = 'numero_chaves_invalido'
        erro += 1
    
    # titulo existe mas ta vazio:

    if 'titulo' in questao:
        verifica = questao['titulo'].strip()
        if verifica == '':
            questao_nova['titulo'] = 'vazio'
            erro += 1

    # verificando nome dos niveis

    if 'nivel' in questao:
        if questao['nivel'] != 'facil' and  questao['nivel'] != 'medio' and  questao['nivel'] != 'dificil':
            questao_nova['nivel'] = 'valor_errado'
            erro += 1
    if 'correta' in questao:
        if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
            questao_nova['correta'] = 'valor_errado'
            erro += 1
    if 'opcoes' in questao:
        opcoes = len(questao['opcoes'].keys())
        
        if opcoes != 4:
            questao_nova['opcoes'] = 'tamanho_invalido'
            erro += 1
        if opcoes == 4:
            contador = 0
            if 'A' in questao['opcoes']:
                contador +=1
            if 'B' in questao['opcoes']:
                contador +=1
            if 'C' in questao['opcoes']:
                contador +=1
            if 'D' in questao['opcoes']:
                contador +=1

            if contador != 4:
                questao_nova['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                erro += 1
            # checando se existe alguma opcao vazia:

            if contador == 4:
                questao_nova['opcoes'] = {}
                for k,v in questao['opcoes'].items():
                    verifica = v.strip()
                    if verifica == '':
                        
                        questao_nova['opcoes'][k] = 'vazia'
                        erro += 1
                if len(questao_nova['opcoes'].keys()) == 0:
                    del questao_nova['opcoes']
                
   
    return questao_nova

print(valida_questao(questao))




