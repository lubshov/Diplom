from datetime import datetime


def Get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
