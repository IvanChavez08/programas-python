# Imprime los numeros de 100 a 1

import os; os.system("clear")

print("\nImprime los nummeros de 100 a 1\n")

n = int(input("Desde donde? "))
p = int(input("Decrementos de ? "))

c = n

while c >= 1 :
    print(c, end=" ")
    c = c - p

print("\nCiclo terminado")