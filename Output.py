# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Output.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
import BisectionMethod
import Secant
import falsePosition
from sympy import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy.optimize import brentq
import fixedPoint
import NewtonRaphson

fig, ax = plt.subplots(figsize=(6, 6), dpi=60)


class Ui_Output(object):
    def __init__(self, mainWindow):
        self.OutputWindow = mainWindow

    def setFunctionUi(self, functionUi):
        self.functionUi = functionUi

    def setValues(self, func: Mul, xl, xu, error, maxIter, method):
        self.func = parse_expr(func)
        self.xl = xl
        self.xu = xu
        self.error = error
        self.maxIter = maxIter
        self.method = method

    def setupUi(self):
        self.OutputWindow.setObjectName("Output")
        self.OutputWindow.resize(620, 480)
        self.OutputWindow.setMinimumSize(QtCore.QSize(620, 480))
        self.OutputWindow.setMaximumSize(QtCore.QSize(620, 480))
        self.centralwidget = QtWidgets.QWidget(self.OutputWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(25, 10, 360, 350))
        self.groupBox.setObjectName("groupBox")
        self.graphCanvas = Canvas(self.groupBox, self.func, self.xl, self.xu, self.method)

        self.iterationsOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.iterationsOutput.setGeometry(QtCore.QRect(400, 30, 200, 330))
        self.iterationsOutput.setObjectName("iterationsOutput")
        self.iterationsOutput.setReadOnly(True)
        self.iterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.iterationsLabel.setGeometry(QtCore.QRect(390, 10, 71, 17))
        self.iterationsLabel.setObjectName("iterationsLabel")
        self.NumberOfIterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumberOfIterationsLabel.setGeometry(QtCore.QRect(25, 370, 300, 25))
        self.NumberOfIterationsLabel.setObjectName("NumberOfIterationsLabel")
        self.executionTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.executionTimeLabel.setGeometry(QtCore.QRect(25, 395, 300, 25))
        self.executionTimeLabel.setObjectName("executionTimeLabel")
        self.approximateRootLabel = QtWidgets.QLabel(self.centralwidget)
        self.approximateRootLabel.setGeometry(QtCore.QRect(25, 420, 300, 25))
        self.approximateRootLabel.setObjectName("approximateRootLabel")
        self.precsionLabel = QtWidgets.QLabel(self.centralwidget)
        self.precsionLabel.setGeometry(QtCore.QRect(25, 445, 300, 25))
        self.precsionLabel.setObjectName("precsionLabel")
        self.newFunctioButton = QtWidgets.QPushButton(self.centralwidget)
        self.newFunctioButton.setGeometry(QtCore.QRect(420, 390, 141, 51))
        self.newFunctioButton.setObjectName("newFunctioButton")
        self.OutputWindow.setCentralWidget(self.centralwidget)
        self.newFunctioButton.clicked.connect(self.newFunctionClicked)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.OutputWindow)

    def newFunctionClicked(self):
        self.functionUi.setupUi()
        self.OutputWindow.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.OutputWindow.setWindowTitle(_translate("Output", "Output"))
        self.iterationsLabel.setText(_translate("Output", "Iterations"))
        self.NumberOfIterationsLabel.setText(_translate("Output", "Number of Iterations"))
        self.executionTimeLabel.setText(_translate("Output", "Execution Time"))
        self.approximateRootLabel.setText(_translate("Output", "Approximate root"))
        self.precsionLabel.setText(_translate("Output", "Relative True Error"))
        self.newFunctioButton.setText(_translate("Output", "Enter New Funcion"))
        self.groupBox.setTitle(_translate("UserInput", "Graph"))
        if self.maxIter == 0:
            self.maxIter = 50
        if self.error == 0:
            self.error = 0.0001

        if self.method == "Bisection":
            z = BisectionMethod.bisection(self.xl, self.xu, self.error, self.maxIter, self.func,
                                          self.iterationsOutput)
            self.NumberOfIterationsLabel.setText(self.NumberOfIterationsLabel.text() + ": " + str(z[1]))
            self.approximateRootLabel.setText(self.approximateRootLabel.text() + f":\t{float(z[0]):.5f}")
            drawXr(z[0])
            trueVal = brentq(self.fun, self.xu, self.xl)

            self.precsionLabel.setText(self.precsionLabel.text() + f": {  (100 * abs(trueVal - z[0]) / trueVal) }\nRelative Absolute Error : {z[3]}")
            self.executionTimeLabel.setText(self.executionTimeLabel.text() + f": {z[2]:.5f}")

        elif self.method == "False-Position":
            z = falsePosition.falsePosition(self.xl, self.xu, self.error, self.maxIter, self.func,
                                            self.iterationsOutput)
            self.NumberOfIterationsLabel.setText(self.NumberOfIterationsLabel.text() + f":  {z[1]}")
            self.approximateRootLabel.setText(self.approximateRootLabel.text() + f":\t{float(z[0]):.5f}")
            drawXr(z[0])
            trueVal = brentq(self.fun, self.xu, self.xl)

            self.precsionLabel.setText(
                self.precsionLabel.text() + f": {(100 * abs(trueVal - z[0]) / trueVal)}\nRelative Absolute Error : {z[3]}")

            self.executionTimeLabel.setText(self.executionTimeLabel.text() + f": {z[2]:.5f}")

        elif self.method == "Fixed Point":
            z = fixedPoint.fixedPt(self.xl, self.xu, self.error, self.maxIter, self.func, self.iterationsOutput)
            print(type(z[0]))

            self.NumberOfIterationsLabel.setText(self.NumberOfIterationsLabel.text() + f":  {z[1]}")

            if z[3] is True:
                self.precsionLabel.setText("!!Method Diverged!!")
                self.approximateRootLabel.setText("")

            else:
                self.approximateRootLabel.setText(self.approximateRootLabel.text() + f":\t{float(z[0]):.5f}")
                self.precsionLabel.setText(f"Relative Absolute Error : {z[4]}")
                drawXr(z[0])
            self.executionTimeLabel.setText(self.executionTimeLabel.text() + f": {z[2]:.5f}")

        elif self.method == "Newton-Raphson":
            z = NewtonRaphson.newtonRaphson(self.xl, self.xu, self.error, self.maxIter, self.func,
                                            self.iterationsOutput)

            self.NumberOfIterationsLabel.setText(self.NumberOfIterationsLabel.text() + f":  {z[1]}")
            self.approximateRootLabel.setText(self.approximateRootLabel.text() + f":\t{float(z[0]):.5f}")
            drawXr(z[0])
            trueVal = brentq(self.fun, self.xu, self.xl)
            self.precsionLabel.setText(
                self.precsionLabel.text() + f": {(100 * abs(trueVal - z[0]) / trueVal)}\nRelative Absolute Error : {z[3]}")

            self.executionTimeLabel.setText(self.executionTimeLabel.text() + f": {z[2]:.5f}")

        elif self.method == "Secant":
            z = Secant.secant(self.xl, self.xu, self.error, self.maxIter, self.func, self.iterationsOutput)
            self.NumberOfIterationsLabel.setText(self.NumberOfIterationsLabel.text() + f":  {z[1]}")
            self.approximateRootLabel.setText(self.approximateRootLabel.text() + f":\t{float(z[0]):.5f}")
            drawXr(z[0])

            trueVal = brentq(self.fun, self.xu, self.xl)
            self.precsionLabel.setText(
                self.precsionLabel.text() + f": {(100 * abs(trueVal - z[0]) / trueVal)}\nRelative Absolute Error : {z[2]}")
            self.executionTimeLabel.setText(self.executionTimeLabel.text() + f": {z[2]:.5f}")

    def fun(self, x):
        return self.func.subs(Symbol('x'), x)


class Canvas(FigureCanvas):
    def __init__(self, parent, func, xl, xu, method):
        global fig, ax
        super().__init__(fig)
        self.setParent(parent)
        x1 = np.linspace(xl, xu, 1000)
        x = Symbol('x')
        y = []

        fig.tight_layout()
        ax.axis("off")
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        for i in x1:
            y.append(func.subs(x, i))
        with mpl.rc_context({'lines.linewidth': 2}):
            plt.plot(x1, y)

        if method == "Fixed Point":
            y1 = []
            funx = x
            for i in x1:
                y1.append(funx.subs(x, i))
            with mpl.rc_context({'lines.linewidth': 2}):
                plt.plot(x1, y1)


def drawXr(xr):
    plt.axvline(x=xr)
    plt.axhline(y=0)
