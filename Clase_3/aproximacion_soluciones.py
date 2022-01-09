"""
Resuelve la ecuación  x^2 = 37 con un error máximo de 0.001
 
"""

def run():
    respuesta = 0
    error = 0.001 
    paso = 0.00000000001
    contador = 0

    while abs(respuesta ** 2 - 37) > error:
        respuesta += paso 
        
        contador += 1 # contandor = contador + 1        

    print(paso)    
    print(contador)
    print(respuesta)



if __name__ == "__main__":
    run()
