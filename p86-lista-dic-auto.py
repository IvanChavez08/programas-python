# Listas de diccionarios / Autos 

autos = [
    {'marca': 'Ford', 'modelo': 'Mustang', 'año': 1964},
    {'marca': 'Vw', 'modelo': 'Jetta', 'año': 2015},
]

autos.append({'marca': 'Chevrolet', 'modelo': 'Captiva', 'año': 2024})

print('Todo:', autos, len(autos))

for auto in autos:
    print(auto)

print('\nDatos en forma de tabla')
for k in autos[0].keys():  # se imprime el titulo de la tabla (las llaves del diccionario)
    print(f'{k:<15}', end='')
print()

for auto in autos:        #para cada auto en autos, imprime los valores de cada auto
    for v in auto.values():
        print(f'{v:<15}', end='')
    print()

print('\nDatos en forma de registros:')
for auto in autos:
    for k, v in auto.items():
        print(f'{k:<12} : {v}') 
    print()  
