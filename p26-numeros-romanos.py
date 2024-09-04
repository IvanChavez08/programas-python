# Dado un numero, muestra el numero en romano

print("Dado un numero, muestra el numero en romano")

numero = int(input("Dame un número entre 1 y 10: "))

if numero == 1:
    romano = "I"
elif numero == 2:
    romano = "II"
elif numero == 3:
    romano = "III"
elif numero == 4:
    romano = "IV"
elif numero == 5:
    romano = "V"
elif numero == 6:
    romano = "VI"
elif numero == 7:
    romano = "VII"
elif numero == 8:
    romano = "VIII"
elif numero == 9:
    romano = "IX"
elif numero == 10:
    romano = "X"
else:
    romano = "Número inválido"

print(f"{numero}: {romano}")
