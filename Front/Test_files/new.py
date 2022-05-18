from PyQt5 import QtCore, QtWidgets
import time



class Function1(QtCore.QThread):
    dataChanged = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.working = True

    def run(self):
        self.dataChanged.emit("Start Function1")
        while self.working:
            for n in range(6):
                self.dataChanged.emit(f"Data Function1: {n}")
                self.msleep(1000)
                if not self.stoped():
                    break
        self.finished.emit(f"finished Function1: {n} -------")

    def stoped(self):
        return self.working
#
# class Function2(QtCore.QThread):
#     dataChanged = QtCore.pyqtSignal(str)
#     finished = QtCore.pyqtSignal(str)
#
#     def __init__(self):
#         super().__init__()
#         self.working = True
#
#     def run(self):
#         while True:
#             for n in range(10, 16):
#                 print(n)
#                 time.sleep(2)
#
#     def run(self):
#         self.dataChanged.emit("Start  Function  22")
#         while self.working:
#             for n in range(10, 16):
#                 self.dataChanged.emit(f"Data  Function  22: {n}")
#                 self.msleep(1000)
#             if not self.stoped():
#                 break
#         self.finished.emit(f"finished  Function  22: {n} -------")
#
#     def stoped(self):
#         return self.working
#
#
# class Function3(QtCore.QThread):
#     dataChanged = QtCore.pyqtSignal(str)
#     finished = QtCore.pyqtSignal(str)
#
#     def __init__(self):
#         super().__init__()
#         self.working = True
#
#     def run(self):
#         while True:
#             n = 'Привет! Я '
#             self.dataChanged.emit(f"Data  Function  333: {n}")
#             self.msleep(3000)
#             # Чекпоинт
#             if not self.stoped():
#                 break
#             n = 'вывожу слова '
#             self.dataChanged.emit(f"Data  Function  333: {n}")
#             self.msleep(3000)
#             # Чекпоинт
#             if not self.stoped():
#                 break
#             n = 'через время'
#             self.dataChanged.emit(f"Data  Function  333: {n}")
#             self.msleep(3000)
#             # Чекпоинт
#             if not self.stoped():
#                 break
#         self.finished.emit(f"finished  Function  333: {n} -------")
#
#     def stoped(self):
#         return self.working


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(165, 270, 70, 23))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 380, 250))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Начать"))


class MyWin(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.start)

        self.function1 = Function1()
        self.function1.dataChanged.connect(self.dataThreads)
        self.function1.finished.connect(self.finishThreads)
        # self.function2 = Function2()
        # self.function2.dataChanged.connect(self.dataThreads)
        # self.function2.finished.connect(self.finishThreads)
        # self.function3 = Function3()
        # self.function3.dataChanged.connect(self.dataThreads)
        # self.function3.finished.connect(self.finishThreads)

    def start(self):
        if self.pushButton.text() == 'Начать':
            self.pushButton.setText('Стоп')
            self.function1.working = True
            self.function1.start()
            # self.function2.working = True
            # self.function2.start()
            # self.function3.working = True
            # self.function3.start()
        else:
            self.pushButton.setText('Начать')
            self.function1.working = False
            # self.function2.working = False
            # self.function3.working = False

    def dataThreads(self, text):
        self.plainTextEdit.appendPlainText(text)

    def finishThreads(self, text):
        self.plainTextEdit.appendPlainText(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())