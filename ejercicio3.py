def longitud_lista(lista):
    longitud_lista = 0
    for item in lista:
        longitud_lista += 1
    return longitud_lista

lista_numeros = [1,2,3,4,5,6,7,8,9,10,11]
len_lista = longitud_lista(lista_numeros)
print(len_lista)

print("\n--------------------------\n")

lista_caracteres = "123456789"
len_string = longitud_lista(lista_caracteres)
print(len_string)
