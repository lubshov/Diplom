from datetime import datetime
from time import sleep
from PyQt5 import QtCore, QtWidgets
import time
from molibden6.diplom2 import measure

def Get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


class FunctionGetdata(QtCore.QThread):
    # Сигналы к которым можно подключиться:
    dataChanged = QtCore.pyqtSignal(dict)

    # finished = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.working = False
        # Программа в начале неактивна
        self.names_rows = ["med", "speed", "speed_2"]

    def run(self):

        while self.working:
            self.msleep(100)
            # print(measure())
            # Изменение переменной передаваемой как сигнал. Передача тестовой функции Get_time()
            self.dataChanged.emit(measure())

        # Изменение переменной передаваемой как сигнал при окончании работы
        self.finished.emit(self.dataChanged)

    def stoped(self):
        return self.working