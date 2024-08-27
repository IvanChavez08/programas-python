#Calcula el número de la suerte dado el año de nacimiento


print("Calcula el número de la suerte a partir del año de nacimiento\n")


año_nacimiento = input("Dame el año de nacimiento (4 dígitos): ")


if len(año_nacimiento) == 4 and año_nacimiento.isdigit():

    dígitos = [int(d) for d in año_nacimiento]
    suma_dígitos = sum(dígitos)


    print("El año de nacimiento es", año_nacimiento)
    print("Dígitos individuales:", ', '.join(map(str, dígitos)))
    print("Número de la suerte:", suma_dígitos)
else:
    print("Introduce un año válido de 4 dígitos")
