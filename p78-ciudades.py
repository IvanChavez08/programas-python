# Lee nombre de ciudades de una lista las acomoda en orden descendente e imrpime cuantas ciudades inician con consonante
import os; os.system("clear")

ciudades = []


while True:
    ciudad = input("Introduce el nombre de una ciudad ($ para terminar): ")
    if ciudad == '$':
        break
    ciudades.append(ciudad)


print(f"Número de ciudades introducidas: {len(ciudades)}")
print("Lista de ciudades: ", ciudades)


ciudades.sort(reverse=True)
print("Lista de ciudades ordenada en orden descendente: ", ciudades)


consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
ciudades_consonantes = [ciudad for ciudad in ciudades if ciudad[0] in consonantes]

print(f"Número de ciudades que inician con una consonante: {len(ciudades_consonantes)}")
print("Ciudades que inician con una consonante: ", ciudades_consonantes)
