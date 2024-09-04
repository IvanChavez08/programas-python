#Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado
  
print("Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado")


nombre = input("Introduce el nombre del estudiante: ")
edad = int(input("Introduce la edad del estudiante: "))
sexo = input("Introduce el sexo del estudiante (h/m): ")
calificacion1 = float(input("Introduce la primera calificación: "))
calificacion2 = float(input("Introduce la segunda calificación: "))
calificacion3 = float(input("Introduce la tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

if sexo == 'm' or sexo == 'M':
    if edad > 21:
        if 8 <= promedio <= 10:
            mensaje = (f"{nombre}, has sido aceptada, tu edad de {edad} y tus calificaciones "
                       f"{calificacion1}, {calificacion2} y {calificacion3}, lo permiten")
        else:
            mensaje = (f"{nombre}, eres mujer, tienes la edad, pero tu promedio no alcanza, "
                       f"solo promedios de 8 a 9.5")
    else:
        mensaje = (f"{nombre}, eres mujer, pero no tienes la edad requerida, solo mayores a 21 años")
else:
    mensaje = f"{nombre}, solo aceptamos mujeres"

print(mensaje)
