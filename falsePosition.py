import sympy as sy
import math
from sympy.plotting import plot
from PyQt5 import QtWidgets
import time


def falsePosition(xl: float, xu: float, es: float, imax: int, func: sy.core.numbers.Float,
                  outputWidget: QtWidgets.QPlainTextEdit):
    startTime = time.time()
    xFunc = sy.Symbol('x')
    a = [0] * (imax + 1)
    b = [0] * (imax + 1)
    ya = [0] * (imax + 1)
    yb = [0] * (imax + 1)
    a[0] = xl
    b[0] = xu
    ya[0] = func.subs(xFunc, a[0])
    yb[0] = func.subs(xFunc, b[0])
    x = [0] * (imax + 1)
    y = [0] * (imax + 1)

    if ya[0] * yb[0] > 0.0:
        print("Func same sign at both ends")
        return
    iter = 0
    for i in range(0, imax):
        iter += 1
        x[i] = b[i] - yb[i] * (b[i] - a[i]) / (yb[i] - ya[i])

        y[i] = func.subs(xFunc, x[i])
        outputWidget.appendPlainText(
            f"iter = {i + 1} xl = {float(a[i]):.5f} xu = {float(b[i]):.5f} xr =  {float(x[i]):.5f} f(xr) = {float(y[i]):.5f}\n")
        if y[i] == 0:
            outputWidget.appendPlainText("Zero Found\n")
            break
        elif y[i] * ya[i] < 0:
            a[i + 1] = a[i]
            ya[i + 1] = ya[i]
            b[i + 1] = x[i]
            yb[i + 1] = y[i]
        else:
            a[i + 1] = x[i]
            ya[i + 1] = y[i]
            b[i + 1] = b[i]
            yb[i + 1] = yb[i]
        ea = abs(x[i] - x[i - 1] / x[i]) * 100
        if i > 1 and ea < es:
            outputWidget.appendPlainText("False position has converged\n")
            break

    if iter >= imax:
        outputWidget.appendPlainText("Zero not found\n")

    endTime = time.time() - startTime
    z = [x[iter - 1], iter, endTime, ea]
    return z

# if __name__ == "__main__":
#     x = sy.Symbol('x')
#     y = x*sy.cos(x)
#
#     xr = falsePosition(1, 2, 0.00001, 50, y)
#
#     if xr is not None:
#         print(f"xr = {float(xr):.5f}")
#     p1 = plot(y, show=False)
#     p1.show()
