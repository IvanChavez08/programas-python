#  Aceptar un estudiante en base a su edad y dos calificaciones
# >=18      c1>=8 y c2>=8

import os; os.system("clear")

print("Universidad patito SA de CV")
print("Aceptar un estudiante en base a su edad y dos calificaciones:\n")

nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))

if edad < 18 :
    print("\nSolo aceptamos mayores de edad")
else:
    print("Dame 2 calificaciones separadas por enter: ")
    c1, c2 = int(input()), int(input())
    if c1<8 or c2<8:
        print("\nSolo aceptamos con calificaciones mayores a 8")
    else:
        print(f"{nombre} bienvenido a la universidad, tu edad {edad} y tus calificaciones {c1}, {c2} lo permiten")

print("\nGracias por utilizar este programa")