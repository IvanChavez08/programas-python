#Verifica si 3 numeros son consecutivos o no

print("Verifica si 3 numeros son consecutivos o no")


n1 = int(input("Dame el primer número: "))
n2 = int(input("Dame el segundo número: "))
n3 = int(input("Dame el tercer número: "))

numeros = [n1, n2, n3]
numeros.sort()

if numeros[1] == numeros[0] + 1 and numeros[2] == numeros[1] + 1:
    print("Los números son consecutivos")
else:
    print("Los números no son consecutivos")
