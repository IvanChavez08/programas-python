#Divide un numero entero de 3 cifras en centenas, decenas y unidades

import os

os.system("clear")

print("Divide un numero entero de 3 cifras en centenas, decenas y unidades \n")
n = int(input("Dame un numero entero de 3 cifras "))

c = n // 100
d = (n - (c * 100) ) // 10
u = (n - (c * 100 + d * 10))

print("El numero original es ", n)
print("Centenas  :", c)
print("Decenas   :", d)
print("Unidades  :", u)

print("\nNumero de la suerte ", c+d+u)