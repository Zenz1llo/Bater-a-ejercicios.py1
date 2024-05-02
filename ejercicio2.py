def func_max(num1, num2, num3):
    # Comparamos los dos primeros
    if num1 == num2:
        mayor = num1
    elif num1 > num2:
        mayor = num1
    else:
        mayor = num2
    # Comparamos el tercero con el mayor de ellos
    if num3 > mayor:
        mayor = num3
    return mayor

numero1 = 1
numero2 = 12
numero3 = 3
numero_mayor = func_max(numero1, numero2, numero3)
print(numero_mayor)
