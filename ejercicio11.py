# import ejercicio10
from ejercicio10 import generar_n_caracteres

def procedimiento(lista):
    for n in lista:
        print(generar_n_caracteres(n))

var_lista = [10,20,50]
procedimiento(var_lista)
