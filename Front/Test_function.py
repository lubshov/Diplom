from datetime import datetime
from time import sleep
from PyQt5 import QtCore, QtWidgets
import time


def Get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


class FunctionGetTime(QtCore.QThread):
    # Сигналы к которым можно подключиться:
    dataChanged = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.working = False
        # Программа в начале неактивна

    def run(self):
        while self.working:
            self.msleep(1)
            # Изменение переменной передаваемой как сигнал. Передача тестовой функции Get_time()
            self.dataChanged.emit(Get_time())

        # Изменение переменной передаваемой как сигнал при окончании работы
        self.finished.emit(Get_time())

    def stoped(self):
        return self.working