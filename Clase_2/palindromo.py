
def run():
    print(" Hola, bienvenido a mi algoritmo para comprobar que tu cadena es un palindromo")
    nombre = input("Ingresa la cadena de texto: ")
    nombre1 = nombre 
    nombre = nombre.upper()
    nombre = nombre.replace(" ", "")
    nombre = nombre.replace(",", "")
    if nombre == nombre[::-1]:
        print("La cadena es un palindromo")
        print("Efectivamente la frase inicial " + nombre1 + " es palindromo")
    else:
        print("La cadena no es un palindromo")

    
if __name__ == "__main__": 
    run()



