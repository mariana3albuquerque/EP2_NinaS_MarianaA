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

    