import time

from sympy import *
from PyQt5 import QtWidgets


def bisection(xl: float, xu: float, es: float, imax: int, func: Float, outputWidget: QtWidgets.QPlainTextEdit):
    startTime = time.time()
    x = Symbol('x')

    if func.subs(x, xu) * func.subs(x, xl) > 0:
        outputWidget.appendPlainText("Can't happen")
        return

    for i in range(0, imax):
        outputWidget.appendPlainText(f"xl = {float(xl):.5f} xu = {float(xu):.5f}\n")
        xr = (xu + xl) / 2
        # mid point
        ea = abs((xu - xl))

        # relative error
        test = (func.subs(x, xl) * func.subs(x, xr))

        if test < 0:
            xu = xr
        else:
            xl = xr

        if test == 0:
            ea = 0
        if ea < es:
            break

    endTime = time.time() - startTime
    ea = abs(ea/xu) * 100
    z = [xr, i+1, endTime, ea]
    return z

#
# if __name__ == "__main__":
#     startTime = time.time()
#     x = Symbol('x')
#     y = x*cos(x)
#     xr = bisection(1, 2, 0.00001, 50, y)
#     endTime = time.time() - startTime
#     p1 = plot(y, show=False)
#     p2 = plot_parametric((xr, x), show=False)
#     p1.append(p2[0])
#     p1.show()
#     print(type(p1))
