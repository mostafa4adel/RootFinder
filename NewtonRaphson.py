from sympy import *
from PyQt5 import QtWidgets
import time

def newtonRaphson(xl: float, xu: float, es: float, maxIter: int, func: Float, outputWidget: QtWidgets.QPlainTextEdit):
    startTime = time.time()
    xGuess = (xl + xu) / 2
    x = Symbol('x')
    dfunc = diff(func, x)

    xr = [0] * (maxIter + 1)
    fx = [0] * (maxIter + 1)
    dfx = [0] * (maxIter + 1)
    xr[0] = xGuess
    fx[0] = float(func.subs(x, xr[0]))
    dfx[0] = float(dfunc.subs(x, xr[0]))

    iter = 0
    for i in range(1, maxIter):
        # print(float(dfx[i - 1]))
        # print(i)
        xr[i] = xr[i - 1] - fx[i - 1] / dfx[i - 1]
        fx[i] = float(func.subs(x, xr[i]))
        dfx[i] = float(dfunc.subs(x, xr[i]))
        outputWidget.appendPlainText(f"i:{i} x:{xr[i]:.20f} f(x):{fx[i]:.5f} f(x)':{dfx[i]:.5f}")
        if abs(float(xr[i]) - float(xr[i - 1])) < es:
            outputWidget.appendPlainText("Converged Successfully")
            break
        iter = i
    er = abs(float(xr[iter-1]) - float(xr[iter - 2]))/float(xr[iter-1]) *100
    endTime = time.time() - startTime
    z = [xr[iter-1], iter, endTime , er]
    if iter >= maxIter:
        outputWidget.setPlainText("Zero Not Found")
    # print(iter)
    return z

#
# if __name__ == "__main__":
#     x = Symbol('x')
#     f = x ** 5 - 11 * x ** 4 + 46 * x ** 3 - 90 * x ** 2 + 81 * x - 27
#     newtonRaphson(0, 2.6, 0.0000001, 100, f)
