
from window import Ui_Dialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import MyWin
from FormToDiplom import MainWindowsToDiplom

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindowsToDiplom()
    w.show()
    sys.exit(app.exec_())


