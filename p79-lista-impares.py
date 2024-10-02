#Llena una lista con los primeros numeros impares, cslcula la suma y el promedio y muestra los que son divisibles entre 3 y los suma

import os; os.system("clear")

n = int(input("Introduce cuántos números impares deseas generar: "))


numeros_impares = [2 * i + 1 for i in range(n)]


suma = sum(numeros_impares)
promedio = suma / n if n > 0 else 0


print(f"Suma de los números impares: {suma}")
print(f"Promedio de los números impares: {promedio}")


divisibles_por_3 = [num for num in numeros_impares if num % 3 == 0]
suma_divisibles = sum(divisibles_por_3)

print(f"Números impares divisibles entre 3: {divisibles_por_3}")
print(f"Suma de los números impares divisibles entre 3: {suma_divisibles}")


elemento_a_buscar = int(input("Introduce un número para buscar en la lista: "))

if elemento_a_buscar in numeros_impares:
    posicion = numeros_impares.index(elemento_a_buscar)
    print(f"El número {elemento_a_buscar} está en la lista en la posición {posicion} ")
else:
    print(f"El número {elemento_a_buscar} no está en la lista ")
