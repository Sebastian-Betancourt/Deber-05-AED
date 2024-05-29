print("*****BIENVENIDO AL BURGER KING *****")
print("Ingrese los datos para la factura electrónica")

nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su número de cédula: ")
correo = input("Ingrese su correo: ")
cantidad = int(input("Ingrese el número de hamburguesas a adquirir: "))

# Datos de entrada
print("Ingrese uno de los siguientes tipos de hamburguesas")
print("1) Sencilla")
print("2) Doble")
print("3) Triple")
tipo = input("Ingrese la opción: ")

if tipo != "1" and tipo != "2" and tipo != "3":
    print("Este tipo de Hamburguesa no existe")
    print("Muchas gracias")
else:
    if tipo == "1":
        valor = cantidad * 1.50
    elif tipo == "2":
        valor = cantidad * 2.50
    else:  # tipo == "3"
        valor = cantidad * 3.25

    print("Ingrese su forma de pago")
    print("1) Tarjeta de crédito")
    print("2) Efectivo")
    forma = input("Ingrese la opción: ")

    if forma != "1" and forma != "2":
        print("No existe ese tipo de pago")
        print("Muchas gracias")
    else:
        if forma == "1":
            subvalor = valor * 0.05  
            valor_final = subvalor + valor 
            print(f"Genial, {nombre}, el precio final es: ${valor_final:.2f}")
        else:  # forma == "2"
            valor_final = valor
            print(f"Genial, {nombre}, el precio final es: ${valor_final:.2f}")
        
        print(f"La factura se enviará a su correo {correo}")
