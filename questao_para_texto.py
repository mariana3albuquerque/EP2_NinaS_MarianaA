def questao_para_texto(questao_dicionario,id):
    r ='\n----------------------------------------\n'
    r += '\nQUESTAO {}\n'.format(id)
    titulo = questao_dicionario['titulo']
    r+='\n{}\n'.format(titulo)
    r+='\nRESPOSTAS:\n'
    for chave,resposta in questao_dicionario['opcoes'].items():
        r+='{0}: {1}\n'.format(chave,resposta)
    r += '\n'
    return r
