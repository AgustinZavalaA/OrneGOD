import re
import math


def euler(y: float, h: float, eq: float) -> float:
    return y + h * eq


def euler_mejorado(y, h, eq0, eq1):
    return y + h * ((eq0 + eq1) / 2)


def replaceEquation(eq: str, x: float, y: float) -> float:
    eq = eq.replace(" ", "")

    eq = eq.replace("^", "**")

    eq = re.sub(r"\)e", ") * " + str(math.e), eq)
    eq = re.sub(r"(\d+)e", r"\1 * " + str(math.e), eq)
    eq = eq.replace("e", str(math.e))

    eq = re.sub(r"\)x", ") * " + str(x), eq)
    eq = re.sub(r"(\d+)x", r"\1 * " + str(x), eq)
    eq = eq.replace("x", str(x))

    eq = re.sub(r"\)y", ") * " + str(y), eq)
    eq = re.sub(r"(\d+)y", r"\1 * " + str(y), eq)
    eq = eq.replace("y", str(y))
    # print(eq)
    return eval(eq)


def main():
    eq = "2*x*y"
    x = 0
    y = 1
    h = 0.1
    yGoal = 0.5

    pasos = int((yGoal - x) / h)

    for _ in range(pasos):
        eq0 = replaceEquation(eq, x, y)
        x = x + h
        y_dot = euler(y, h, eq0)
        y = euler_mejorado(y, h, eq0, replaceEquation(eq, x, y_dot))
    print(y)


if __name__ == "__main__":
    main()
