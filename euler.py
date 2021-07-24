import numpy as np
import re


def euler(y: float, h: float, eq: float) -> float:
    return y + h * eq


def replaceEquation(eq: str, x: float, y: float) -> float:
    eq = eq.replace(" ", "")

    eq = eq.replace("^", "**")

    eq = re.sub(r"\)x", ") * " + str(x), eq)
    eq = re.sub(r"(\d+)x", r"\1 * " + str(x), eq)
    eq = eq.replace("x", str(x))

    eq = re.sub(r"\)y", ") * " + str(y), eq)
    eq = re.sub(r"(\d+)y", r"\1 * " + str(y), eq)
    eq = eq.replace("y", str(y))
    # print(eq)
    return eval(eq)


def main():
    # ec = input("EC og: ")

    # x0 = float(input("xd: "))
    # y0 = float(input("y : "))

    # h = float(input("h : "))

    # ygoal = float(input("h : "))
    eq = "2x-3y+1"
    x = 1
    y = 5
    h = 0.05
    ygoal = 1.2

    for i in np.arange(x, ygoal, h):
        y = euler(y, h, replaceEquation(eq, x, y))
        x = x + h

    print(y)


if __name__ == "__main__":
    main()
