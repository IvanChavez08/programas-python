# Lee el numero de mes y los dias y los imprime

import os; os.system("clear")

nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


dias_meses = [31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31]


mes = int(input("Introduce el número del mes (1-12): "))


if 1 <= mes <= 12:
    mes_index = mes - 1 
    print(f"{nombres_meses[mes_index]}, {dias_meses[mes_index]} días")
else:
    print("Número de mes inválido ")
