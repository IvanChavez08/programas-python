# Calcula el promedio de 5 calificaciones

print("Calcula el promedio de 5 calificaciones")


calificacion1 = float(input("Dame la primera calificación: "))
calificacion2 = float(input("Dame la segunda calificación: "))
calificacion3 = float(input("Dame la tercera calificación: "))
calificacion4 = float(input("Dame la cuarta calificación: "))
calificacion5 = float(input("Dame la quinta calificación: "))


promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5


if promedio > 0 and promedio < 6:
    mensaje = "Quedas reprobado"
elif promedio >= 6 and promedio < 7:
    mensaje = "Pasas de panzazo"
elif promedio >= 7 and promedio < 8:
    mensaje = "Muy bien, puedes mejorar"
elif promedio >= 8 and promedio < 9:
    mensaje = "Excelente, sigue así"
elif promedio >= 9 and promedio <= 10:
    mensaje = "Perfecto, tu esfuerzo valió la pena"
else:
    mensaje = "Calificación fuera del rango"

# Mostrar el promedio y el mensaje
print(f"Promedio: {promedio:.2f}, {mensaje}")
