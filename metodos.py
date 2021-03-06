import numpy as np
import re
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
from newton import newton, graficar_newton
from euler import euler, eval_equation
from math import sin, cos, tan, exp
import datetime


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
    print("UNIVERSIDAD POLITÉCNICA DE VICTORIA")
    print("Solución de ecuaciones por métodos númericos")
    print("Integrantes del equipo:\n- 1930120 - Agustín Zavala Arias\n- 1930346 - Roberto Eduardo Higuera Sánchez")
    print("Materia: Matemáticas para Ingeniería II")
    print("Docente: Ing. Juan Manuel Ornelas Llerena")
    print("Fecha: " + str(datetime.date.today()) + "\n")
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
        x = float(input("f( ) = "))
        y = float(input("f(" + str(x) + ") = "))
        h = float(input("h = "))
        ygoal = float(input("meta y = "))

        x_axis.append(x)
        y_axis.append(y)

        number_steps = int((ygoal - x) / h) + 1
        iter = 0
        print("Iter   x     y    yReal      absErr       relErr")
        for _ in range(number_steps):
            y = euler(y, h, eval_equation(eq, x, y))
            x = x + h
            iter += 1
            yReal = exp(-0.2 + 0.2 * x ** 2)
            error_absoluto = yReal - y
            error_relativo = error_absoluto / abs(yReal)
            print(
                "%d   %.2f    %.2f    %.4f    %.4f     %.4f" % (iter, x, y, yReal, yReal - y, (yReal - y) / abs(yReal))
            )
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

        iter = 0
        print("Iter   x    f(x)   f'(x)      yReal    absErr     relErr")

        xi = x0
        while True:
            # print(xi)
            xi, fp = newton(f, xi)
            if fp == 0:
                break
            yReal = exp(-0.2 + 0.2 * xi ** 2)
            print(
                "%d   %.2f    %.2f    %.2f     %.4f    %.4f     %.4f"
                % (iter, xi, f(xi), fp, yReal, yReal - f(xi), ((yReal - f(xi)) / abs(yReal)))
            )
            iter += 1
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
