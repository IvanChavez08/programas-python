# Eleva un numero base a su exponente

import os; os.system("clear")

base = int(input("Base       ? "))
exp = int(input("exponentes  ? "))

#print(f"La base {base} elevado a la {exp} es {base ** exp}")

p = 1
for i in range(exp):
    p = p * base
print(f"La base {base} elevado a la {exp} es {p}")



p = 1
for _ in range(exp):
    p = p * base
else:
    print("\nEl ciclo termino correctamente")

    
print(f"\nLa base {base} elevado a la {exp} es {p}")