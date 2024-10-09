# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena

import os; os.system("clear")


cadena = input("Introduce una cadena: ")


conteo_caracteres = {}


for caracter in cadena:
    if caracter in conteo_caracteres:
        conteo_caracteres[caracter] += 1  
    else:
        conteo_caracteres[caracter] = 1   


print('Conteo de caracteres:', conteo_caracteres)
