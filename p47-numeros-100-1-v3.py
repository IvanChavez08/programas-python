# Imprime numeros del 1 al 100 usando for

import os; os.system("clear")

"""print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(1,10,3)))
print(list(range(10,0,-1)))"""

n = int(input("Desde donde deseas descender ? "))
i = int(input("Decrementos de ? "))

for x in range (n,0, -i):
    print(x, end=" ")