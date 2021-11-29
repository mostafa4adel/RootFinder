from sympy import *
from PyQt5 import QtWidgets
import time


def secant(x0, x1, es, maxIter, func: Float, outputWidget: QtWidgets.QPlainTextEdit):
    startTime = time.time()
    x = Symbol('x')
    step = 1
    condition = True
    x2 = 0
    while condition:
        if func.subs(x, x0) == func.subs(x, x1):
            outputWidget.appendPlainText('Divide by zero error!')
            break
        f0 = func.subs(x, x0)
        f1 = func.subs(x, x1)
        x2 = x0 - (x1 - x0) * f0 / (f1 - f0)
        outputWidget.appendPlainText('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, func.subs(x, x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > maxIter:
            outputWidget.appendPlainText('Not Convergent!')
            break

        condition = abs(func.subs(x, x2)) > es

    endTime = time.time() - startTime
    z = [x2, step, endTime]
    return z
#
# if __name__ == "__main__":
#     x = Symbol('x')
#     f = x ** 3 - 5 * x - 9
#     secant(2, 3, 0.0000001, 100, f)
