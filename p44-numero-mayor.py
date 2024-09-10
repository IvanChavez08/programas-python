# Calcula el número mayor de una serie de números introducidos

import os

while True:
    os.system("clear")  

    print("Introduce una serie de números para encontrar el mayor")
    print("Introduce 0 para finalizar la entrada de números")

    mayor = None  

    while True:
        
        numero = float(input("\nIntroduce un número: "))

        if numero == 0:
            break

        if mayor is None or numero > mayor:
            mayor = numero

    if mayor is not None:
        print(f"\nEl número mayor introducido es: {mayor}")
    else:
        print("\nNo se introdujeron números válidos.")


    if input("\nDeseas continuar (S/N)").upper().startswith("N") : break


print("\nProceso terminado")
