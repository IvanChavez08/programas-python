# Calcula la temperatura convertida de grados centígrados a grados farenheit de un rango de valores introducidos por el usuario

import os

while True:
    os.system("clear")  

    
    temp_inicial = int(input("Introduce la temperatura inicial en grados Celsius: "))
    temp_final = int(input("Introduce la temperatura final en grados Celsius: "))

    if temp_inicial > temp_final:
        print("La temperatura inicial debe ser menor o igual a la temperatura final ")
        continue

    print(f"\nConversión de temperaturas de Celsius a Fahrenheit:")
    celsius = temp_inicial
    while celsius <= temp_final:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
        celsius += 1  


    if input("\nDeseas continuar (S/N)").upper().startswith("N") : break

print("\nProceso terminado")
