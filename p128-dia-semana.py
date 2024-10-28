#Pide un numero entero entre 1 y 7 y devuelve el dia de la semana con letra

import os;os.system('clear')

def obtener_dia_semana():
    numero = int(input("Ingresa un número del 1 al 7: "))
    if numero < 1 or numero > 7:
        return "Número inválido, debe estar entre 1 y 7"
    
    dias = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
    
    return dias[numero - 1]

resultado = obtener_dia_semana()
print(f"El día de la semana es: {resultado}")
