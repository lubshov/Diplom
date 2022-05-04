from datetime import datetime
from time import sleep

def Get_time1():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def Get_time():
    while True:
        sleep(1)
        print(Get_time1())