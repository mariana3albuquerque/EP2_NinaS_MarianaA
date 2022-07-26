lista = [
  {
    'titulo': 'Qual o resultado da operação 57 + 32?',
    'nivel': 'facil',
    'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    'correta': 'C'
  },
  {
    'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'
  },
  {
    'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
    'nivel': 'medio',
    'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
    'correta': 'C'
  }
]
def transforma_base(lista):
    if lista == []:
        return {}
    transformada = {}
    transformada['facil'] = []
    transformada['medio'] = []
    transformada['dificil'] = []
    for i in range(len(lista)):
        if lista[i]['nivel'] == 'facil':
            transformada['facil'].append(lista[i])
        elif lista[i]['nivel'] == 'medio':
            transformada['medio'].append(lista[i])
        else:
            transformada['dificil'].append(lista[i])
    if len(transformada['facil']) == 0:
        del transformada['facil']
    if len(transformada['medio']) == 0:
        del transformada['medio']
    if len(transformada['dificil']) == 0:
        del transformada['dificil']
    return transformada

print(transforma_base(lista))