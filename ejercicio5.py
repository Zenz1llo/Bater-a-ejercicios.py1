
# letra_a_entero_dict = {"a": 0,
#                        "b": 1, 
#                        "c": 2, 
#                        "d": 3,
#                        "e": 4, 
#                        "f": 5,
#                        "g": 6, 
#                        "h": 7,
#                        "i": 8, 
#                        "j": 9}

# entero_a = letra_a_entero_dict["a"]
# print(entero_a)

# entero_c = letra_a_entero_dict["b"]
# print(entero_c)

# entero_j = letra_a_entero_dict["j"]
# print(entero_j)

letras_str = "abcdefghij"

# letra_a_entero_dict = {}
# for n, letra in enumerate(letras_str):
#     letra_a_entero_dict[letra] = n

# print(letra_a_entero_dict)

letra_a_entero_dict = {letra: n for n, letra in enumerate(letras_str)}
print(letra_a_entero_dict)

entero_a = letra_a_entero_dict["a"]

print(entero_a)

entero_c = letra_a_entero_dict["b"]
print(entero_c)

entero_j = letra_a_entero_dict["j"]
print(entero_j)







