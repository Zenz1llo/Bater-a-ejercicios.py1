"""
Definir una función que dada una lista,
retorne los elementos unicos de la lista:

Ej:
[1,2,2,3,4,4,5] -> [1,2,3,4,5]

Sin usar set() ni unique()
"""
def get_unique_elements(lista):
    
    # Lista a popular
    lista_unica = []

    # Sacamos rangos
    len_lista = len(lista)
    rango_1 = range(len_lista)
    
    # Declaramos un flag
    for n_1 in rango_1:
        if lista[n_1] != lista[n_1 + 1]:
            

lista = [1,2,2,2,3,4,4,5]

lista_unica = get_unique_elements(lista)
print(lista_unica)


