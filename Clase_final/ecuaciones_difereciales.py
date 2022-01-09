import math

def fun(x,y):
    return math.sin(x*y)


def run():

    """
    sólo se resuelve ecuaciones diferenciales de la forma dy/dx = f(x,y)"""
    x0 = 0
    y0 = 0
    h = 0.1
    xn = x0
    yn = y0

    for i in range(100):        

        k1 = fun(xn, yn)
        k2 = fun(xn + 0.5 * h, yn + 0.5 * h * k1)
        k3 = fun(xn + 0.5 * h, yn + 0.5 * h * k2)
        k4 = fun(xn + h, yn + h * k3)
       
        xn = xn + h
        yn = yn + 1/6 * h * (k1 + 2 * k2 + 2* k3 + k4 )
        print(f"x {i+1} = {xn} || y {i+1} = {yn}")


if __name__ == "__main__":
    run()