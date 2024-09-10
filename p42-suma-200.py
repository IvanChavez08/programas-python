# Calcula la suma de números introducidos por el usuario hasta que la suma sea >= 200, muestra cuantos números fueron introducidos y la suma de estos.

import os

while True:
    os.system("clear")  

    suma = 0
    conteo = 0

    print("Introduce números para calcular la suma hasta que sea >= 200")
    print("El proceso se detendrá cuando la suma sea al menos 200")

    while suma < 200:
        
        numero = float(input("\nIntroduce un número: "))
        
        suma += numero
        conteo += 1

    print(f"\nLa suma de los números introducidos es: {suma}")
    print(f"Cantidad de números introducidos: {conteo}")

    
    if input("\nDeseas continuar (S/N)").upper().startswith("N") : break


print("\nProceso terminado")
