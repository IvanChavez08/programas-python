# desea imprimir los números impares del 1 a n de forma ascendente e imprime la suma de esos números impares

import os

while True:
    os.system("clear")  


    n = int(input("Introduce el número hasta el cual imprimir los números impares: "))

    if n < 1:
        print("Introduce un número mayor o igual a 1 ")
        continue

    suma_impares = 0
    numero = 1  
    print(f"Números impares desde 1 hasta {n}: ")

    while numero <= n:
        print(numero, end=" ")
        suma_impares += numero
        numero += 2  
    
    print(f"\nSuma de los números impares: {suma_impares}")

    if input("\nDeseas continuar (S/N)").upper().startswith("N") : break


print("\nProceso terminado")
