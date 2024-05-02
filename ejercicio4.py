
def es_una_vocal(letra):
    flag_vocal = False
    if letra in ["a","e","i","o","u"]:
        flag_vocal = True
    return flag_vocal
    
letra_ej = "j"
letra_ej_es_vocal = es_una_vocal(letra_ej)
print(letra_ej_es_vocal)
