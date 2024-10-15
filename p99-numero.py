# Operaciones entre conjuntos de números
import os; os.system("clear")

numeros_A = {50, 60, 70, 80, 90, 100, 200}
numeros_B = {60, 90, 100, 300, 400, 500}
numeros_C = {10, 20, 60, 90, 70, 100, 600, 700}

print('Conjunto A:', numeros_A)
print('Conjunto B:', numeros_B)
print('Conjunto C:', numeros_C)


union_A_B = numeros_A | numeros_B
union_B_C = numeros_B | numeros_C
diferencia_A_C = numeros_A - numeros_C
diferencia_simetrica_B_C = numeros_B ^ numeros_C
interseccion_B_C = numeros_B & numeros_C

print('\nUnión de A y B (A | B):', union_A_B)
print('Unión de B y C (B | C):', union_B_C)
print('Diferencia de A y C (A - C):', diferencia_A_C)
print('Diferencia simétrica de B y C (B ^ C):', diferencia_simetrica_B_C)
print('Intersección de B y C (B & C):', interseccion_B_C)


print('\n¿A es subconjunto de B?', numeros_A.issubset(numeros_B))
print('¿C es subconjunto de A?', numeros_C.issubset(numeros_A))
print('¿100 está en A?', 100 in numeros_A)
print('¿60 está en A, y en B y en C?', 60 in numeros_A and 60 in numeros_B and 60 in numeros_C)
print('¿900 no está en C?', 900 not in numeros_C)
