import time

from sympy import *


def bisection(xl: float, xu: float, es: float, imax: int, func: float):
    if func.subs(x, xu) * func.subs(x, xl) > 0:
        print("Can't happen")
        return

    for i in range(0, imax):
        print(f"xl = {xl} xu = {xu}")
        xr = (xu + xl) / 2
        # mid point
        if xl != 0:
            ea = abs((xu - xl) / xl)
        else:
            ea = 10000
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

    print(f"Root = {xr} Iterations = {i}")
    return xr


if __name__ == "__main__":
    startTime = time.time()
    x = Symbol('x')
    y = x ** 2 - 1
    xr = bisection(0, 3, 0.00001, 50, y)
    endTime = time.time() - startTime
    p1 = plot(y, show=False)
    p2 = plot_parametric((xr, x), show=False)
    p1.append(p2[0])
    p1.show()
    print(type(p1))
