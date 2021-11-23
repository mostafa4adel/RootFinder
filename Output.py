# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Output.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import numpy as np

import ChooseFunction
from PyQt5 import QtCore, QtGui, QtWidgets
import BisectionMethod
import falsePosition
from sympy import *
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

fig, ax = plt.subplots(figsize=(6, 6), dpi=60)


class Ui_Output(object):
    def __init__(self, mainWindow):
        self.OutputWindow = mainWindow

    def setFunctionUi(self, functionUi):
        self.functionUi = functionUi

    def setValues(self, func: Mul, xl, xu, error, maxIter):
        self.func = func
        self.xl = xl
        self.xu = xu
        self.error = error
        self.maxIter = maxIter

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
        self.graphCanvas = Canvas(self.groupBox, self.func)

        self.iterationsOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.iterationsOutput.setGeometry(QtCore.QRect(400, 30, 200, 330))
        self.iterationsOutput.setObjectName("iterationsOutput")
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
        self.precsionLabel.setText(_translate("Output", "Precision"))
        self.newFunctioButton.setText(_translate("Output", "Enter New Funcion"))
        self.groupBox.setTitle(_translate("UserInput", "Graph"))


class Canvas(FigureCanvas):
    def __init__(self, parent, func):
        global fig, ax
        super().__init__(fig)
        self.setParent(parent)
        x1 = np.linspace(-2, 2, 100)
        x = Symbol('x')
        y = []
        func = parse_expr(func)
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