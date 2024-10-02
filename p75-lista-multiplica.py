# Lee dos listas con 5 elementos y las multiplica

import os; os.system("clear")

lista1 = []
lista2 = []
resultado = []


print("Introduce los primeros 5 elementos: ")
for i in range(5):
    elemento = float(input(f'Elemento {i+1}: '))
    lista1.append(elemento)


print("Introduce los otros 5 elementos: ")
for i in range(5):
    elemento = float(input(f'Elemento {i+1}: '))
    lista2.append(elemento)

# Multiplicar las listas
for i in range(5):
    resultado.append(lista1[i] * lista2[i])

# Imprimir las tres listas
print("\nPrimera lista: ", lista1)
print("Segunda lista: ", lista2)
print("Resultado de la multiplicación: ", resultado)
