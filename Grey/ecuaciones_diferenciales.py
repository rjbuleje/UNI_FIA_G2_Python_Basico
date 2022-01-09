import math

def run():
    """ dy/dx = y + x """


    x0 = 0
    y0 = 0

    def fun(x, y):
        return math.sin(x)

    h = 0.5

    xn = x0
    yn = y0
    print(xn, yn)

    for i in range(20):
        k1 = fun(xn, yn)
        k2 = fun(xn + 1/2 * h, yn + 1/2 * h * k1)
        k3 = fun(xn + 1/2 * h, yn + 1/2 * h * k2)
        k4 = fun(xn + h, yn + h * k3)
        yn = yn + 1/6 * h * (k1 + 2* k2 + 2 * k2 +k4)
        xn = xn + h
        print(xn, yn)











if __name__ == "__main__":
    run()