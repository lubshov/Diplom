# -*- coding: utf-8 -*-
from Test_function import Get_time, FunctionGetTime
# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setMinimumSize(QtCore.QSize(500, 500))
        Dialog.setMaximumSize(QtCore.QSize(500, 500))
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(160, 290, 161, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Button_StartGetTime = QtWidgets.QPushButton(self.formLayoutWidget)
        self.Button_StartGetTime.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Button_StartGetTime)
        self.Button_StopGetTime = QtWidgets.QPushButton(self.formLayoutWidget)
        self.Button_StopGetTime.setObjectName("pushButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Button_StopGetTime)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 100, 141, 81))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_StartGetTime.setText(_translate("Dialog", "????????????"))
        self.Button_StopGetTime.setText(_translate("Dialog", "????????"))
        self.label.setText(_translate("Dialog", "??????????: -"))




class MyWin(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Button_StartGetTime.clicked.connect(self.start)
        self.Button_StopGetTime.clicked.connect(self.stop)
        self.FunctionGetTime = FunctionGetTime()
        self.FunctionGetTime.dataChanged.connect(self.dataThreads)
        self.FunctionGetTime.finished.connect(self.finishThreads)
        self.FunctionGetTime.working = False

    def start(self):
        # print("test")

        self.FunctionGetTime.working = True
        self.FunctionGetTime.start()

    def stop(self):
        self.FunctionGetTime.working = False
        self.FunctionGetTime.stoped()

    def dataThreads(self, text):
        self.label.setText("??????????: " + text)

    def finishThreads(self, text):
        self.label.setText("??????????: " + text)


def create(text):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
