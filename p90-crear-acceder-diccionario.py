#Crear diccionario con los dias de la semana

import os; os.system("clear")


dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado',
    7: 'Domingo'
}


print('Diccionario de días:', dias)


primer_elemento = dias[1]
ultimo_elemento = dias[7]
quinto_elemento = dias.get(5)
septimo_elemento = dias.get(7)

print('Primer elemento:', primer_elemento)
print('Último elemento:', ultimo_elemento)
print('Quinto elemento:', quinto_elemento)
print('Séptimo elemento:', septimo_elemento)


print('Diccionario completo:', dias)
