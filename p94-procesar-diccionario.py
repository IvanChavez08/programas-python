# Se crea diccionario con nombres y sueldos, los suma y calcula promedio

import os; os.system("clear")


nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]


trabajadores = dict(zip(nombres, sueldos))


print('Diccionario de trabajadores:', trabajadores)


print('\nIteracion usando keys():')
for nombre in trabajadores.keys():
    print(nombre)

print('\nIteracion usando values():')
for sueldo in trabajadores.values():
    print(sueldo)

print('\nIteracion usando llave y valor:')
for nombre in trabajadores.keys():
    print(f'{nombre}: {trabajadores[nombre]}')

print('\nIteracion usando items():')
for nombre, sueldo in trabajadores.items():
    print(f'{nombre}: {sueldo}')


suma_sueldos = sum(trabajadores.values())
print('\nSuma de los sueldos : ', suma_sueldos)


promedio_sueldos = suma_sueldos / len(trabajadores)
print(f'Promedio de los sueldos : ', promedio_sueldos)
