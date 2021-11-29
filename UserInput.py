# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInput.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import os

from sympy import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import Output
import ChooseFunction


class Ui_UserInput(object):
    def __init__(self, mainWindow):
        self.UserInputWindow = mainWindow

    def setBackUi(self, backUi):
        self.backUi = backUi

    def setOutputUiForBisectionAndFalse(self, outputUi):
        self.outputUi = outputUi

    def setMethod(self, method: str):
        self.method = method

    def setupUi(self):
        self.UserInputWindow.setObjectName("UserInput")
        self.UserInputWindow.resize(400, 250)
        self.UserInputWindow.setMinimumSize(QtCore.QSize(400, 250))
        self.UserInputWindow.setMaximumSize(QtCore.QSize(400, 250))
        self.centralwidget = QtWidgets.QWidget(self.UserInputWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.functionLabel = QtWidgets.QLabel(self.centralwidget)
        self.functionLabel.setGeometry(QtCore.QRect(10, 40, 67, 25))
        self.functionLabel.setObjectName("functionLabel")
        self.lowerGuessLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowerGuessLabel.setGeometry(QtCore.QRect(10, 80, 90, 25))
        self.lowerGuessLabel.setObjectName("lowerGuessLabel")
        self.upperGuessLabel = QtWidgets.QLabel(self.centralwidget)
        self.upperGuessLabel.setGeometry(QtCore.QRect(205, 80, 90, 25))
        self.upperGuessLabel.setObjectName("upperGuessLabel")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(10, 120, 41, 25))
        self.errorLabel.setObjectName("errorLabel")
        self.maxIterLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxIterLabel.setGeometry(QtCore.QRect(10, 160, 141, 25))
        self.maxIterLabel.setObjectName("maxIterLabel")
        self.functionInput = QtWidgets.QLineEdit(self.centralwidget)
        self.functionInput.setGeometry(QtCore.QRect(100, 40, 280, 25))
        self.functionInput.setObjectName("functionInput")
        self.lowerInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lowerInput.setGeometry(QtCore.QRect(100, 80, 91, 25))
        self.lowerInput.setDecimals(5)
        self.lowerInput.setMinimum(-100000000.0)
        self.lowerInput.setMaximum(100000000.0)
        self.lowerInput.setObjectName("doubleSpinBox")
        self.upperInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.upperInput.setGeometry(QtCore.QRect(289, 80, 91, 25))
        self.upperInput.setDecimals(5)
        self.upperInput.setMinimum(-100000000.0)
        self.upperInput.setMaximum(100000000.0)
        self.upperInput.setObjectName("doubleSpinBox_2")
        self.errorInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.errorInput.setGeometry(QtCore.QRect(100, 120, 91, 25))
        self.errorInput.setDecimals(6)
        self.errorInput.setMinimum(-1.0)
        self.errorInput.setMaximum(100000000.0)
        self.errorInput.setObjectName("doubleSpinBox_3")
        self.maxIterInput = QtWidgets.QSpinBox(self.centralwidget)
        self.maxIterInput.setGeometry(QtCore.QRect(170, 160, 75, 25))
        self.maxIterInput.setObjectName("spinBox")
        self.evaluateButton = QtWidgets.QPushButton(self.centralwidget)
        self.evaluateButton.setGeometry(QtCore.QRect(100, 200, 90, 40))
        self.evaluateButton.setObjectName("evaluateButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 50, 25))
        self.backButton.setObjectName("backButton")
        self.getFromFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.getFromFileButton.setGeometry(QtCore.QRect(220, 200, 101, 40))
        self.getFromFileButton.setObjectName("getFromFileButton")
        self.UserInputWindow.setCentralWidget(self.centralwidget)
        self.backButton.clicked.connect(self.backButtonClicked)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.UserInputWindow)
        self.evaluateButton.clicked.connect(self.evaluateButtonClicked)
        self.getFromFileButton.clicked.connect(self.fileDialog)

    def backButtonClicked(self):
        self.backUi.setupUi()
        self.UserInputWindow.show()

    def evaluateButtonClicked(self):
        unacceptable = False
        unacceptable = self.lowerInput.value() >= self.upperInput.value() or not validateFunction(
            self.functionInput.text(), self.lowerInput.value(), self.upperInput.value())

        if unacceptable:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wrong Input")
            msg.setInformativeText('Input Proper Values')
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        self.outputUi.setValues(self.functionInput.text(), self.lowerInput.value(), self.upperInput.value(),
                                self.errorInput.value(), self.maxIterInput.value(), self.method)
        self.outputUi.setupUi()
        self.UserInputWindow.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.UserInputWindow.setWindowTitle(_translate("UserInput", "MainWindow"))
        self.functionLabel.setText(_translate("UserInput", "Function"))
        self.lowerGuessLabel.setText(_translate("UserInput", "Lower Guess"))
        self.upperGuessLabel.setText(_translate("UserInput", "Upper Guess"))
        self.errorLabel.setText(_translate("UserInput", "Error"))
        self.maxIterLabel.setText(_translate("UserInput", "Maximum Iterations"))
        self.evaluateButton.setText(_translate("UserInput", "Evaluate"))
        self.backButton.setText(_translate("UserInput", "Back"))
        self.getFromFileButton.setText(_translate("UserInput", "Get From File"))

    def fileDialog(self):
        fileName = self.getFileName()
        i = 0
        try:
            with open(fileName) as f:
                lines = f.readlines()

                for line in lines:
                    i = i + 1
                    line = line.replace('\n', '')
                if i != 0:
                    self.functionInput.setText(lines[0])
                if i > 0:
                    self.lowerInput.setValue(float(lines[1].split(' ')[0]))
                    self.upperInput.setValue(float(lines[1].split(' ')[1]))
                if i > 1:
                    self.errorInput.setValue(float(lines[2].split(' ')[0]))
                    self.maxIterInput.setValue(int(lines[2].split(' ')[1]))
        except:
            pass



    def getFileName(self):
        file_filter = 'Data File (*.txt)'
        response = QFileDialog().getOpenFileName(
            parent=self.centralwidget,
            caption='Select Data  File',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.txt)'
        )

        return response[0]


def validateFunction(func: str, x0, x1):
    try:
        function = parse_expr(func)

        if len(function.atoms(Symbol)) > 1 or len(function.atoms(Symbol)) == 0:
            return False
        if 'x' not in str(function):
            return False
        if function.subs(Symbol('x'), x0) * function.subs(Symbol('x'), x1) > 0:
            print("Bad input")
            return False
        return True
    except:
        return False
