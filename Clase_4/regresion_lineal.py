X = (1, 2, 3, 4, 5 , 8, 1, 10)
Y = (7, 8, 9, 10, 11, 10, 20, 100)

def run():
    x_promedio = 0
    y_promedio = 0

    for i in range(len(X)):
        x_promedio = x_promedio + X[i]
        y_promedio = y_promedio + Y[i]

    x_promedio = x_promedio / len(X)
    y_promedio = y_promedio / len(Y)

    arriba = 0
    abajo = 0

    for i in range(len(X)):
        arriba = arriba + (X[i] - x_promedio) * (Y[i] - y_promedio)
        abajo = abajo + (X[i] - x_promedio) ** 2

    pendiente = arriba / abajo

    punto_paso = y_promedio - pendiente * x_promedio

    pendiente = round(pendiente, 2)
    punto_paso = round(punto_paso, 2)

    print(f' Y = {punto_paso} + X * {pendiente}')





    



if __name__ == "__main__":
    run()