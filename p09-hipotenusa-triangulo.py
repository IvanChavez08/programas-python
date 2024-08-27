#Calcula la hipotenusa de un triangulo rectangulo dadas las longitudes de sus lados

import math

lado1 = float(input("Introduce la longitud del primer lado: "))
lado2 = float(input("Introduce la longitud del segundo lado: "))


hipotenusa = math.sqrt(lado1 * lado1 + lado2 * lado2)


print(f"La longitud de la hipotenusa es: {hipotenusa}")
