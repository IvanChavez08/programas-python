print("Universidad Patito SA de CV")
print("Sistema de Inscripción Congreso de Sistemas")

total_ventas = 0

while True:
    
    tipo_usuario = int(input("\nTipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500 ? "))
    
    if tipo_usuario == 1:
        precio_usuario = 100
        usuario_str = "Alumno"
        descuento_porcentaje = 20
    elif tipo_usuario == 2:
        precio_usuario = 200
        usuario_str = "Trabajador"
        descuento_porcentaje = 10
    elif tipo_usuario == 3:
        precio_usuario = 500
        usuario_str = "Docente"
        descuento_porcentaje = 5
    else:
        print("Tipo de usuario inválido")
        continue
    
    
    tipo_paquete = int(input("Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900 ? "))
    
    if tipo_paquete == 1:
        precio_paquete = 600
        paquete_str = "Solo conferencias"
    elif tipo_paquete == 2:
        precio_paquete = 800
        paquete_str = "Con eventos sociales"
    elif tipo_paquete == 3:
        precio_paquete = 900
        paquete_str = "Con kit de acceso"
    else:
        print("Tipo de paquete inválido")
        continue
    
    
    cantidad = int(input("Cantidad ? "))
    
    
    subtotal = (precio_usuario + precio_paquete) * cantidad
    
    if subtotal > 5000:
        descuento = subtotal * (descuento_porcentaje / 100)
    else:
        descuento = 0
    
    total = subtotal - descuento
    
    
    print(f"Tu pedido fue: {cantidad}, Tipo de usuario: {usuario_str}, Tipo de paquete: {paquete_str}")
    print(f"Subtotal: {subtotal} con un descuento de: {descuento} ({descuento_porcentaje}%) y un total de {total}")
    
    
    total_ventas += total
    
    
    if input("\nDeseas continuar (S/N)").upper().startswith("N") : break


print(f"\nImporte Total de la Venta: {total_ventas:.2f}")
print("\nProceso terminado ...")
