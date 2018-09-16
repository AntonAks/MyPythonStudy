"""
@decorators (simple examples)
"""
from datetime import datetime


def decor_func_1(func):
    def wrapped():
        print(datetime.now())
        func()
        print(datetime.now())
    return wrapped


@decor_func_1
def say_hello():
    print('Hello')


print('First example:\n')
say_hello()


def decor_func_2(func):
    def wrapped(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        finish = datetime.now()
        print(f"Running time: {finish - start}")
    return wrapped


@decor_func_2
def my_func(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    print(my_list)


print('\nSecond example:\n')
my_func(5000*10)
