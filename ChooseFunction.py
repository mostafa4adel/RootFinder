# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseFunction.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import this

from PyQt5 import QtCore, QtWidgets
import UserInput


class Ui_ChooseMethod(object):
    def __init__(self, mainWindow, userInputUi: UserInput.Ui_UserInput):
        self.ChooseMethodWindow = mainWindow
        self.userInputUi = userInputUi

    def setupUi(self):
        self.ChooseMethodWindow.setObjectName("ChooseMethod")
        self.ChooseMethodWindow.resize(400, 250)
        self.ChooseMethodWindow.setMinimumSize(QtCore.QSize(400, 250))
        self.ChooseMethodWindow.setMaximumSize(QtCore.QSize(400, 250))
        self.centralwidget = QtWidgets.QWidget(self.ChooseMethodWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.methodComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.methodComboBox.setGeometry(QtCore.QRect(100, 90, 200, 25))
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.chooseMethodButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseMethodButton.setGeometry(QtCore.QRect(140, 130, 120, 25))
        self.chooseMethodButton.setObjectName("chooseMethodButton")
        self.ChooseMethodWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.chooseMethodButton.clicked.connect(self.chooseMethodClicked)
        QtCore.QMetaObject.connectSlotsByName(self.ChooseMethodWindow)

    def chooseMethodClicked(self):
        self.userInputUi.setMethod(self.methodComboBox.currentText())

        self.userInputUi.setupUi()
        self.ChooseMethodWindow.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ChooseMethodWindow.setWindowTitle(_translate("ChooseMethod", "MainWindow"))
        self.methodComboBox.setItemText(0, _translate("ChooseMethod", "Bisection"))
        self.methodComboBox.setItemText(1, _translate("ChooseMethod", "False-Position"))
        self.methodComboBox.setItemText(2, _translate("ChooseMethod", "Fixed Point"))
        self.methodComboBox.setItemText(3, _translate("ChooseMethod", "Newton-Raphson"))
        self.methodComboBox.setItemText(4, _translate("ChooseMethod", "Secant"))
        self.chooseMethodButton.setText(_translate("ChooseMethod", "Choose Method"))
