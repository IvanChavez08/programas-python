#Procesa notas de entre 0 y 100

import os; os.system("clear")


notas = []
suma_notas = 0


while True:
    nota = float(input('Introduce una nota (0 para terminar): '))
    if nota == 0:
        break
    if 0 <= nota <= 100:
        notas.append(nota)
        suma_notas += nota
    else:
        print("La nota debe estar entre 0 y 100 ")


cantidad_notas = len(notas)

if cantidad_notas > 0:
    promedio = suma_notas / cantidad_notas
    notas_menores_promedio = [n for n in notas if n < promedio]
    nota_maxima = max(notas)
    nota_minima = min(notas)


    print(f'Cantidad de notas: {cantidad_notas}')
    print('Notas:', notas)
    print(f'Suma de notas: {suma_notas}')
    print(f'Promedio: {promedio:.2f}')
    print(f'Notas menores al promedio ({promedio:.2f}):', notas_menores_promedio)
    print(f'Cantidad de notas menores al promedio: {len(notas_menores_promedio)}')
    print(f'Nota máxima: {nota_maxima}')
    print(f'Nota mínima: {nota_minima}')
else:
    print("No se ingresaron notas ")
