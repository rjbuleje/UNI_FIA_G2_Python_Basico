import random as rd
import math


def run():
    numero_usuario = int(input("Ingrese un número natural entre el 1 y el 100: "))
    numero_aleatorio = rd.randint(1, 101)
    numero = math.pi
    print(numero)

    while numero_usuario != numero_aleatorio:
        if numero_usuario < numero_aleatorio:
            print("El número ingresado es menor")
            numero_usuario = int(input("Vuelva a ingresar otro número: "))
        elif numero_usuario > numero_aleatorio:
            print("El número ingresado es mayor")
            numero_usuario = int(input("Vuelva a ingresar otro número: "))
        
    print("Ganaste")


if __name__ == "__main__":
    run()