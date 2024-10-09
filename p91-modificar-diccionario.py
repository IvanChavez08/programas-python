# Crea diccionario con los paises y modifica unos con update y otros con []

import os; os.system("clear")


paises = {
    'Argentina': 100,
    'Brasil': 200,
    'Colombia': 300,
    'Chile': 400,
    'Ecuador': 500,
    'Bolivia': 600,
    'Jamaica': 700
}


print('Diccionario de países:', paises)


paises['Brasil'] = 250 
paises['Chile'] = 450  
paises.update({'Bolivia': 650})  
paises.update({'Jamaica': 750})   


print('Diccionario modificado:', paises)
