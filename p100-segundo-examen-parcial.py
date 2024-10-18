# Segundo examen parcial - Computación Aplicada - MITA - Iván Neftalí Chávez Flores 

import os; os.system("clear")

print("Mueblería Muebles Dico")
print("Sistema de Procesamiento de Empleados")

empleados = []

while True:
    nombre = input("Captura de datos de los empleados * para terminar: ")
    if nombre.lower() == '*':
        break

    edad = int(input("Ingrese la edad del empleado: "))
    sexo = input("Ingrese el sexo del empleado (h/m): ").lower()
    pasatiempos = input("Ingrese los pasatiempos del empleado (separados por comas): ")
    sueldo = float(input("Ingrese el sueldo del empleado: "))

    empleado = {
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "pasatiempos": pasatiempos.split(","),
        "sueldo": sueldo
    }
    empleados.append(empleado)

print("\nTabla de datos:")
print(f"{'Nombre':<10} {'Edad':<5} {'Sexo':<5} {'Salario':<10} {'Pasatiempos':<30}")
for emp in empleados:
    print(f"{emp['nombre']:<10} {emp['edad']:<5} {emp['sexo']:<5} {emp['sueldo']:<10,.2f} {', '.join(emp['pasatiempos']):<30}")

total_empleados = len(empleados)
hombres = sum(1 for emp in empleados if emp['sexo'] == 'h')
mujeres = total_empleados - hombres

conteo_pasatiempos = {}
for emp in empleados:
    for p in emp['pasatiempos']:
        p = p.strip()  
        conteo_pasatiempos[p] = conteo_pasatiempos.get(p, 0) + 1

suma_edades = sum(emp['edad'] for emp in empleados)
promedio_edad = suma_edades / total_empleados if total_empleados > 0 else 0

suma_sueldos = sum(emp['sueldo'] for emp in empleados)
promedio_sueldo = suma_sueldos / total_empleados if total_empleados > 0 else 0

mayor_edad = max(empleados, key=lambda x: x['edad'], default=None)
menor_edad = min(empleados, key=lambda x: x['edad'], default=None)

print("\nResumen:")
print(f"Empleados: {total_empleados}")
print(f"Mujeres: {mujeres}")
print(f"Hombres: {hombres}")

pasatiempos_str = ", ".join(f"{p}/{conteo}" for p, conteo in conteo_pasatiempos.items())
print(f"Pasatiempos: {pasatiempos_str}")

print(f"Edad -> suma: {suma_edades}, Promedio: {promedio_edad:.1f}")
print(f"Sueldo -> suma: {suma_sueldos:,.2f}, promedio: {promedio_sueldo:,.2f}")

if mayor_edad:
    print(f"{mayor_edad['nombre']} de {mayor_edad['edad']} es el mayor.")
if menor_edad:
    print(f"{menor_edad['nombre']} de {menor_edad['edad']} es el menor.")
