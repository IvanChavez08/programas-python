# Convierte pulgadas a centímetros y metros a pies

import os;os.system('clear')

def convertir(opcion):
    if opcion == '1':
        pulgadas = float(input("Ingresa el número de pulgadas: "))
        centimetros = pulgadas * 2.54
        print(f"{pulgadas} pulgadas son {centimetros:.2f} centímetros ")
    elif opcion == '2':
        metros = float(input("Ingresa el número de metros: "))
        pies = metros * 3.281
        print(f"{metros} metros son {pies:.2f} pies ")
    else:
        print("Opción inválida ")

while True:
    print("\nMenú de Conversión: ")
    print("1. Pulgadas a Centímetros ")
    print("2. Metros a Pies ")
    print("3. Salir ")
    
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == '3':
        print("Saliste del programa ")
        break
    else:
        convertir(opcion)
