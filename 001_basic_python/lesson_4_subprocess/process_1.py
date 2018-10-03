from time import sleep
import datetime

print('Started FIRST Process')
for i in range(0, 10):
    print(f'Hello from process 1 {datetime.datetime.now()}')
    sleep(1)
