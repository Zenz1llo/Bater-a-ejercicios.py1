def func_max(num1, num2):
    if num1 == num2:
        mayor = None
    elif num1 > num2:
        mayor = num1
    else:
        mayor = num2
    return mayor

numero1 = 1
numero2 = 2
numero_mayor = func_max(numero1, numero2)
print(numero_mayor)
