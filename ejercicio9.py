

def superposicion(lista1, lista2):
    flag = False
    i = 0
    j = 0
    rango_1 = range(len(lista1))
    for n_1 in rango_1:
        elemento_1 = lista1[n_1]
        rango_2 = range(n_1, len(lista1))
        for n_2 in rango_2:
            elemento_2 = lista2[n_2]
            if elemento_1 == elemento_2:
                flag = True
    return flag
