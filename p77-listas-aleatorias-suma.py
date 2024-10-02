# Genera listas de 10 numeros aleatorios y sumo los impares

import os, random; os.system("clear")


lista1 = [random.randint(1, 100) for _ in range(10)]
lista2 = [random.randint(1, 100) for _ in range(10)]


suma_impares = [x + y for x, y in zip(lista1, lista2) if x % 2 != 0 and y % 2 != 0]


print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Suma de impares: ", suma_impares)
