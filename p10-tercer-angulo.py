# Dados dos angulos de un triangulo calcula el 3er angulo


angulo1 = float(input("Introduce el valor del primer angulo en grados: "))
angulo2 = float(input("Introduce el valor del segundo angulo en grados: "))


angulo3 = 180 - (angulo1 + angulo2)

50
print(f"El valor del tercer ángulo es: {angulo3:.2f} grados")
