from time import sleep
import datetime

print('Started SECOND Process')
for i in range(0, 10):
    print(f'Hello from process 2 {datetime.datetime.now()}')
    sleep(1)

