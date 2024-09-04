# Imprime numeros hasta llegar a una suma de 100

import os;os.system("clear")

print("\nImprime numeros hasta llegar a una suma de 100")


c = 0
s = 0

while c < 300:
    c = c + 1
    s = s + c
    print(c,end=" ")
    if s >= 10000:
        break


print(f"\nLa suma es {s}, sumando {c} numeros")