# Imprime los números pares desde 100 hasta n, además deberá e imprime la suma de esos números pares

import os

while True:
    os.system("clear")  

    
    n = int(input("Introduce el número hasta el cual deseas imprimir los números pares: "))

    if n < 100:
        print("Introduce un número mayor o igual a 100 ")
        continue

    suma_pares = 0
    numero = 100  
    print(f"Números pares desde 100 hasta {n}: ")

    while numero <= n:
        print(numero, end=" ")
        suma_pares += numero
        numero += 2  

    print(f"\nSuma de los números pares: {suma_pares}")

    if input("\nDeseas continuar (S/N)").upper().startswith("N") : break


print("\nProceso terminado")
