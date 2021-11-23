import sympy as sy
import math
from sympy.plotting import plot


def falsePosition(xl: float, xu: float, es: float, imax: int, func: sy.core.numbers.Float):
    xFunc = sy.Symbol('x')
    a = [0] * imax
    b = [0] * imax
    ya = [0] * imax
    yb = [0] * imax
    a[0] = xl
    b[0] = xu
    ya[0] = func.subs(xFunc, a[0])
    yb[0] = func.subs(xFunc, b[0])
    x = [0] * imax
    y = [0] * imax

    if ya[0] * yb[0] > 0.0:
        print("Func same sign at both ends")
        return
    iter = 0
    for i in range(0, imax):
        iter += 1
        x[i] = b[i] - yb[i] * (b[i] - a[i]) / (yb[i] - ya[i])

        y[i] = func.subs(xFunc, x[i])
        print(f"{i + 1}\t{float(a[i]):.5f}\t{float(b[i]):.5f}\t{float(x[i]):.5f}\t{float(y[i]):.5f}")
        if y[i] == 0:
            print("Zero Found")
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

        if i > 1 and abs(x[i] - x[i - 1]) < es:
            print("False position has converged")
            break

    if iter >= imax:
        print("Zero not found")

    n = len(x)
    print("step\txl\txu\txr\tf(xr)")
    for i in range(0, iter):
        print(f"{i + 1}\t{float(a[i]):.5f}\t{float(b[i]):.5f}\t{float(x[i]):.5f}\t{float(y[i]):.5f}")
        if a[i + 1] == 0 and b[i + 1] == 0 and x[i + 1] == 0 and y[i + 1] == 0:
            break
    return x[iter - 1]


if __name__ == "__main__":
    x = sy.Symbol('x')
    y = x ** 3 - x ** 2 + 2
    xr = falsePosition(-200, 300, 0.00001, 50, y)
    print(f"xr = {float(xr):.5f}")
    p1 = plot(y, show=False)
    p1.show()
