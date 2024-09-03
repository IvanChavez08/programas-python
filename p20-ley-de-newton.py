#Calcular la segunda ley de newton (f = m * a)

import os; os.system("clear")
print("Calcular la segunda ley de newton (f = m * a)")
print("[F] fuerza             f = m * a ")
print("[M] masa               m = f / a ")
print("[A] aceleracion        a = f / m ")
op = input("Elije: ").upper()

if op == "F":
    print("\nCalculando la fuerza...")
    m = float(input("Dame la masa: "))
    a = float(input("Dame la aceleración: "))
    f = m * a
    print(f"La fuerza es: {f}")
elif op == "M":
    print("\nCalculando la masa...")
    f = float(input("Dame la fuerza: "))
    a = float(input("Dame la aceleración: "))
    m = f / a
    print(f"La masa es: {m}")
elif op == "A":
    print("\nCalculando la aceleración...")
    f = float(input("Dame la fuerza: "))
    m = float(input("Dame la masa: "))
    a = f / m
    print(f"La aceleración es: {m}")
else:
    print("\nOpción inválida")

print("\nProceso terminado")