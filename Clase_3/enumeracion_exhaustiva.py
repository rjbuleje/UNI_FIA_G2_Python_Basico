"""
Necesitamos crear un algoritmo basado en enumeración exhaustiva que me permita
encontrar el mayor cuadrado perfecto menor al número dado.
Se trabaja en los naturales positvos. 
"""

def run():
    
    numero_dado = int(input("Ingresa un número: "))
    respuesta = 1
    while respuesta ** 2 < numero_dado:
        respuesta += 1 #respuesta = respuesta + 1

    print((respuesta-1) ** 2)


    for i in range(1, numero_dado):
        if i ** 2 >= numero_dado:
            i = i - 1 
            break 

    print(i ** 2)








if __name__ == "__main__":
    run()




