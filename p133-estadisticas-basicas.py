# Calcula mayor, menor, media, varianza y desviación estándar

import os;os.system('clear')

def leer_arreglo():
    entrada = input("Dame los números (separados por espacio): ")
    lista_numeros = list(map(int, entrada.split()))
    return lista_numeros

def mayor(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def media(lista):
    return sum(lista) / len(lista)

def varianza(lista):
    media_lista = media(lista)
    return sum((x - media_lista) ** 2 for x in lista) / len(lista)

def desviacion_estandar(lista):
    return varianza(lista) ** 0.5

lista_numeros = leer_arreglo()

media_valor = media(lista_numeros)
mayor_valor = mayor(lista_numeros)
menor_valor = menor(lista_numeros)
varianza_valor = varianza(lista_numeros)
desviacion_valor = desviacion_estandar(lista_numeros)

print(f"Lista de números: {lista_numeros}")
print(f"La media: {media_valor:.3f}")
print(f"Mayor de los datos: {mayor_valor}")
print(f"Menor de los datos: {menor_valor}")
print(f"Varianza: {varianza_valor:.3f}")
print(f"Desviación estándar: {desviacion_valor:.3f}")
