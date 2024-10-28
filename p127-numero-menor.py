#Pide 3 números enteros y devuelve el menor

import os;os.system('clear')

def encontrar_menor():
    num1 = int(input("Ingresa el primer número entero: "))
    num2 = int(input("Ingresa el segundo número entero: "))
    num3 = int(input("Ingresa el tercer número entero: "))

    menor = min(num1, num2, num3)
    
    return menor

resultado = encontrar_menor()
print(f"El menor de los tres números es: {resultado}")
