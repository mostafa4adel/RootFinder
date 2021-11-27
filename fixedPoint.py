from sympy import *
import time
from PyQt5 import QtWidgets


def fixedPt(xl: float, xu: float, es: float, iter_max: int, func: Float, outputWidget: QtWidgets.QPlainTextEdit):
    startTime = time.time()
    x = Symbol('x')

    xr = (xl + xu) / 2
    iter = 0
    z = [] * 4
    while True:
        tempX = xr
        xr = func.subs(x, tempX)


        outputWidget.appendPlainText(f"step : {iter+1}, x: {xr}\n")
        if xr != 0:
            ea = abs((xr - tempX) / xr) * 100
        iter = iter + 1

        if ea < es or iter > iter_max:
            outputWidget.appendPlainText("done")
            break
    endTime = time.time() - startTime

    z = [xr, iter, endTime, False]

    if iter > iter_max:
        z[3] = True
        outputWidget.appendPlainText("Diverged :(")
    return z

#
# if __name__ == "__main__":
#     x = Symbol('x')
#     f = x ** 2 - 1
#     xr = fixedPt(0, 4, 0.0000001, 4, f)
#     print(f"{float(xr):.5f}")
