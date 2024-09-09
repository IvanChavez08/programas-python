# Calcula e imprime los numeros de la conjetura de collatz


import os


while(True) :

    os.system("clear")
    num = int(input("Dame un numero entero positivo: "))

    while num !=1 :
        print(num, end=" ")
        if num % 2 == 0 :
               num = num // 2
        else:
            num = num * 3 + 1
    print(num, end= " ")

    if input("\n\nDeseas continuar (S/N)").upper().startswith("N") : break

print("\nProceso terminado")