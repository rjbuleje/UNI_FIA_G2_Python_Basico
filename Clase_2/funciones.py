
def convertir(tipo, soles, moneda,  funcion_ejemplo):
    funcion_ejemplo()
    monto_conversor = soles * tipo
    monto_conversor = round(monto_conversor, 1)
    print("El monto en " + moneda + "es: " + str(monto_conversor))


def saludar_persona():
    print("Robert")
    

#comentario
print("""Bienvenido al conversor de monedas
Ingresa el monto en soles a cambiar
Elije la moneda extranjera de tu preferencia:
dolar
euro
peso_argentino
peso_chileno
peso_colombiano
""")


soles = input("Ingrese monto de la moneda en soles: ")
soles = int(soles)
moneda_extranjera = input("Escriba dolar o euro o peso_argentino o peso_chileno o peso_colombiano: ")
if moneda_extranjera == "dolar":
    tipo_de_cambio = 0.24
    convertir(tipo_de_cambio, soles, moneda_extranjera, saludar_persona)
elif moneda_extranjera == "euro":
    tipo_de_cambio = 0.21
    convertir(tipo_de_cambio, soles, moneda_extranjera)
elif moneda_extranjera == "peso_argentino":
    tipo_de_cambio = 23.79
    convertir(tipo_de_cambio, soles, moneda_extranjera)
elif moneda_extranjera == "peso_chileno":
    tipo_de_cambio = 192.38
    convertir(tipo_de_cambio, soles, moneda_extranjera)
elif moneda_extranjera == "peso_colombiano":
    tipo_de_cambio = 946.69000000000
    convertir(tipo_de_cambio, soles, moneda_extranjera)
else:
    print("Elija una opción correcta")

