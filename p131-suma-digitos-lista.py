import os;os.system('clear')

def leer_arreglo():
    entrada = input("Dame los números separados por espacio: ")
    lista_numeros = list(map(int, entrada.split()))
    return lista_numeros

def suma_digitos(numero):
    return sum(int(digit) for digit in str(numero))

def suma_digitos_lista(lista):
    return [suma_digitos(num) for num in lista]

lista_numeros = leer_arreglo()

lista_sumas = suma_digitos_lista(lista_numeros)

print(f"La lista de números original: {lista_numeros}")
print(f"La lista con las sumas de dígitos de los números: {lista_sumas}")
