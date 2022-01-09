I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
A = [[2, 3, 9], [+9, 4, 8], [8, 55, 100]]

def generador_matrices_respuesta(filas, columnas):
    matriz = []
    
    for i in range(filas):
        matriz.append([0] * columnas)
    
    return matriz


def suma_matrices(matriz_a, matriz_b, multiplacando = 1):
    """
    Función que te permite sumar o restar matriz
    Esta función recibe 3 parámetros
    La primera matriz
    La segunda matriz
    Y un factor que permite diferenciar la operación
    Si desea sumar, puede omitir el tercer parámetro, de los contrario ingrese -1
    En caso de resta, la matriz que ingrese primero se le restará la matriz que ingrese segunda
    """
    filas = len(matriz_b)
    columnas = len(matriz_a[0])
    respuesta = generador_matrices_respuesta( filas, columnas)

    for i in range(filas):
        for j in range(columnas):
            respuesta[i][j] = matriz_a[i][j] + matriz_b[i][j] * multiplacando
    
    return respuesta

    

def multiplicacion_matrices(primera_matriz, segunda_matriz):
    filas = len(primera_matriz)
    columnas = len(segunda_matriz[0])
    recorrido = len(segunda_matriz)
    respuesta = generador_matrices_respuesta(filas, columnas)

    for i in range(filas):
        for j in range(columnas):
            # inicio el acumulador
            respuesta[i][j] = 0        
            for k in range(recorrido):
                # acumular suma del producto de elementos de ambas matrices
                respuesta[i][j] += primera_matriz[i][k] * segunda_matriz[k][j]

    return respuesta

def determinante():
    pass


def matriz_adjunta():
    pass


def matriz_inversa():
    pass


def run():

    matriz_b = multiplicacion_matrices(A, I)
    print((matriz_b))



if __name__ == "__main__":
    run()