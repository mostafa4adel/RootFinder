import sys
import ChooseFunction
import UserInput
import Output


from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    userInputUi = UserInput.Ui_UserInput(mainWindow)
    chooseFunctionUi = ChooseFunction.Ui_ChooseMethod(mainWindow, userInputUi)
    chooseFunctionUi.setupUi()
    outputUiForBisectionAndFalse = Output.Ui_Output(mainWindow)
    userInputUi.setBackUi(chooseFunctionUi)
    userInputUi.setOutputUiForBisectionAndFalse(outputUiForBisectionAndFalse)
    mainWindow.show()
    outputUiForBisectionAndFalse.setFunctionUi(chooseFunctionUi)

    sys.exit(app.exec_())
