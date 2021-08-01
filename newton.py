from scipy.misc import derivative
import matplotlib.pyplot as plt


def newton(f, x):
    return x - f(x) / derivative(f, x)


def graficar_newton(f, x_inicial, x_final):
    x_axis = []
    y_axis = []

    diferencia = abs(x_inicial - x_final)
    x = x_final - diferencia
    y = f(x)
    x_axis.append(x)
    y_axis.append(y)

    for i in range(100):
        x += diferencia / 50
        y = f(x)
        x_axis.append(x)
        y_axis.append(y)

    plt.plot(x_axis, y_axis)
    plt.show()


def main():
    eq = "x**2"
    x0 = 2
    tope_y = 0
    margen_error = 0.001

    # create lambda from function string
    f = lambda x: eval(eq)

    xi = x0
    while True:
        # print(xi)
        xi = newton(f, xi)
        if f(xi) > tope_y - margen_error and f(xi) < tope_y + margen_error:
            break

    print("R = " + str(xi))
    graficar_newton(f, x0, xi)


if __name__ == "__main__":
    main()