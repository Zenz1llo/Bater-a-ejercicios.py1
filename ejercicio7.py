from typing import List

def suma(lista_numeros: List[float]) -> float:
    suma = 0.0
    for numero in lista_numeros:
        suma += numero
    return suma

resultado_suma = suma([1.2,3.4,5.0,8.])
print(resultado_suma)


def multiplicacion(lista_numeros: List[float]) -> float:
    multiplicacion = 1.0
    for numero in lista_numeros:
        multiplicacion *= numero
    return multiplicacion

resultado_multiplicacion = multiplicacion([1.2,3.4,5.0,8.])
print(resultado_multiplicacion)

