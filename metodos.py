import numpy as np
import re
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
from newton import newton, graficar_newton
from euler import euler, eval_equation


def clean_string(eq):
    eq = eq.replace(" ", "")

    eq = eq.replace("^", "**")

    eq = re.sub(r"\)e", ") * " + str(math.e), eq)
    eq = re.sub(r"(\d+)e", r"\1 * " + str(math.e), eq)
    eq = eq.replace("e", str(math.e))

    eq = re.sub(r"\)x", ") * x", eq)
    eq = re.sub(r"(\d+)x", r"\1 * x", eq)

    eq = re.sub(r"\)y", ") * y", eq)
    eq = re.sub(r"(\d+)y", r"\1 * y", eq)
    # print(eq)
    return eq


def main():
    while menu():
        pass


def menu():
    print("Calculadora de metodos Euler y Newton")
    print("1 .- EULER")
    print("2 .- NEWTON")
    print("3 .- SALIR")

    opt = int(input("> "))
    if opt == 1:
        x_axis, y_axis = [], []
        eq = input("f(x, y) = ")
        eq = clean_string(eq)
        x = float(input("f( )"))
        y = float(input("f(" + str(x) + ") = "))
        h = float(input("h = "))
        ygoal = float(input("meta y = "))

        x_axis.append(x)
        y_axis.append(y)

        number_steps = int((ygoal - x) / h) + 1

        for _ in range(number_steps):
            y = euler(y, h, eval_equation(eq, x, y))
            x = x + h
            x_axis.append(x)
            y_axis.append(y)

        print(y)
        plt.plot(x_axis, y_axis)
        plt.show()
        input()

    elif opt == 2:
        eq = input("f(x) = ")
        eq = clean_string(eq)
        x0 = float(input("x0 = "))
        tope_y = float(input("y esperada = "))
        margen_error = float(input("margen error = "))

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

        input()
    else:
        return False

    return True


if __name__ == "__main__":
    main()