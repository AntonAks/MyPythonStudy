import time
import threading
import datetime


class myThread (threading.Thread):
    def __init__(self, name, func):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func

    def run(self):
        print("Start " + self.name)
        self.func()
        print("Finish " + self.name)


def func_1():
    for i in range(0, 15):
        print(f'from function 1 : {i}')
        time.sleep(1)


def func_2():
    for i in range(0, 15):
        print(f'from function 2 : {i}')
        time.sleep(1)


# Creation of new thread with execute functions
thread1 = myThread("Tread 1", func_1)
thread2 = myThread("Tread 2", func_2)

# Starting threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exit from script")

