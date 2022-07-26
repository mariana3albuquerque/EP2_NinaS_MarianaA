def questao_para_texto(questao_dicionario,id):
    r ='\n----------------------------------------\n'
    r += 'QUESTAO {}\n'.format(id)
    titulo = questao_dicionario['titulo']
    r+='\n{}\n'.format(titulo)
    r+='\nRESPOSTAS:\n'
    for chave,resposta in questao_dicionario['opcoes'].items():
        r+='{0}: {1}\n'.format(chave,resposta)
    r += '\n'
    return r
print(questao_para_texto({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}, 5) )