import os;os.system('clear')

def leer_arreglo():
    entrada = input("Dame los números (separados por espacio): ")
    lista_numeros = list(map(int, entrada.split()))
    return lista_numeros

def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return factorial

def factoriales_lista(lista):
    return [calcular_factorial(num) for num in lista]

lista_numeros = leer_arreglo()

lista_factoriales = factoriales_lista(lista_numeros)

print(f"La lista de números originales: {lista_numeros}")
print(f"La lista con los factoriales: {lista_factoriales}")
