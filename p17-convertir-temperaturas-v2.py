#Convertir temperaturas de centigrados a farenheit y viceversa

print("Convertir temperaturas de centigrados a farenheit y viceversa\n")
print("[1] Convertir farenheit a celcius ")
print("[2] Convertir celcius a farenheit ")
print("[3] Salir ")
op = int(input("Elige: "))

if op == 1:
    print("Convirtiendo de farehnheit a celcius ")
    temp = float(input("Dame los grados farenheit: "))
    res = (temp -32) * 5 / 9
    print(f"{temp} Farenheit equivale a {res} celcius")
elif op == 2:
    print("Convirtiendo de centigrados a farenheit")
    temp = float (input("Dame los grados celsius: "))
    res = (temp * 9 / 5) + 32
    print(f"{temp} celcius equivale a {res} farenheit")
elif op == 3:
    print("\nTe vas porque tu quieres...gracias")
else:
    print("Opcion erronea")

print("\nProceso terminado")
    