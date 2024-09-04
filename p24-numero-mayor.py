# Dado 3 numeros, verifica cual es mayor

print("Dado 3 numeros, verifica cual es mayor")


n1 = int(input("Dame el primer número: "))
n2 = int(input("Dame el segundo número: "))
n3 = int(input("Dame el tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

print(f"El mayor de los números {n1}, {n2}, {n3} es el {mayor}")
