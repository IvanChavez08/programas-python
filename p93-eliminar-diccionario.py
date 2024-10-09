# Crea un diccionario con municipios y luego elimina algunos con del, otro con pop(), otros con popitem() y otro on clear()

import os; os.system("clear")


municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalpa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}


print('Diccionario de municipios:', municipios)


del municipios['Apozol']
print('Eliminar Apozol : ', municipios)


fresnillo_value = municipios.pop('Fresnillo')
print('Eliminar Fresnillo : ', municipios)


momax_item = municipios.popitem()
print('Eliminar Momax : ', municipios)


municipios.clear()
print('Eliminar todos : ', municipios)
