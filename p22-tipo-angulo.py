# Muestra el tipo de angulo en base a su magnitud
# <90 agudo,  =90 es recto,  <180 obtuso,  =180 llano,  >180 y >360 concavo,   =360 cerrado

import os; os.system("clear")

print("Muestra el tipo de angulo en base a su magnitud\n")

angulo = int(input("Dame el angulo: "))

if angulo >= 0 and angulo <= 360:
    print(f"El angullo tiene {angulo} grados, entonces es: ", end="")
    if angulo < 90:
        print("Agudo")
    elif angulo == 90:
        print("Recto")
    elif angulo > 90 and angulo <180:
        print("Obtuso")
    elif angulo == 180:
        print("Llano")
    elif angulo >180 and angulo <360:
        print("Concavo")
    else:
        print("Cerrado o completo")
else:
    print("\nEl angulo está fuera de rango")