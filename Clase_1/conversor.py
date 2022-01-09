
#comentario
print("""Bienvenido al conversor de monedas
Ingresa el monto en soles a cambiar
Elije la moneda extranjera de tu preferencia:
dolar
euro
""")

soles = input("Ingrese monto de la moneda en soles: ")
soles = int(soles)
moneda_extranjera = input("Escriba dolar o euro: ")
if moneda_extranjera == "dolar":
    monto_conversor = soles / 4.08
    print("La monto en " + moneda_extranjera + "es: " + str(monto_conversor)) 
elif moneda_extranjera == "euro": 
    monto_conversor = soles / 4.79
    print("La monto en " + moneda_extranjera + "es: " + str(monto_conversor)) 
else:
    print("Por favor vuelva a iniciar el programar")

