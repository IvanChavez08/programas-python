#Calcula el volumen de un cilindro dado su radio y altura

import math


radio = float(input("Introduce el radio del cilindro: "))


altura = float(input("Introduce la altura del cilindro: "))


volumen = math.pi * (radio ** 2) * altura


print(f"El volumen del cilindro es: {volumen:.2f}")
