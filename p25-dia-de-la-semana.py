# Dado un número, muestra el día de la semana

print("Dado un número, muestra el día de la semana")

numero = int(input("Dame un número entre 1 y 7: "))

if numero == 1:
    dia = "Domingo"
elif numero == 2:
    dia = "Lunes"
elif numero == 3:
    dia = "Martes"
elif numero == 4:
    dia = "Miércoles"
elif numero == 5:
    dia = "Jueves"
elif numero == 6:
    dia = "Viernes"
elif numero == 7:
    dia = "Sábado"
else:
    dia = "Día inválido"

print(f"{numero}: {dia}")
