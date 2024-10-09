#Crea un diccionario con ventas y luego agrega elementos con [] y con update()

import os; os.system("clear")


ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}


print('Diccionario de ventas:', ventas)


ventas['Rocio'] = 2500        
ventas['Mateo'] = 1567        
ventas.update({'Andrea': 9567})  
ventas.update({'Miguel': 1234})   


print('Diccionario de ventas modificado:', ventas)
