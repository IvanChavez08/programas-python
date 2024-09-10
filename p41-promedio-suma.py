# Calcula la suma y el promedio de una serie de números introducidos hasta introducir 0 y cuenta cuantos números se introdujeron.

import os

while True:
    os.system("clear")  

    suma = 0
    conteo = 0

    print("Introduce números para calcular la suma, el promedio y contar cuántos números se introdujeron ")
    print("Introduce 0 para finalizar la entrada de números ")

    while True:
    
        numero = float(input("\nIntroduce un número: "))

        if numero == 0:
            break

        suma += numero
        conteo += 1

    if conteo > 0:
        promedio = suma / conteo
    else:
        promedio = 0

    print(f"\nSuma de los números introducidos: {suma}")
    print(f"Cantidad de números introducidos: {conteo}")
    print(f"Promedio de los números introducidos: {promedio}")

    
    if input("\nDeseas continuar (S/N)").upper().startswith("N") : break


print("\nProceso terminado")
