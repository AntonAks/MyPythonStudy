
# simple example
def my_function(a, b):
    # Returns 5% of the sum a & b
    return sum((a, b)) * 0.05


print(f"1. simple example result is: {my_function(30, 50)}")


# example with *args
def my_function_2(*args):
    return sum(args)*0.05


print(f"2. example with *args result is: {my_function_2(30, 50, 80, 100)}")


# 2 example with *args
def my_function_args(*args):
    for i in args:
        # print(str(i) + ' type is ' + str(type(i)))
        print(f"{i} parameter has {type(i)} type")


print(f"3. example with *args 2 result is: ")
my_function_args(40, 143.7, 'some string', True)


# example with **kwargs
def my_function_kwargs(**kwargs):
    print(f"{kwargs} has {type(kwargs)}")


print(f"4. example with **kwargs result is: ")
my_function_kwargs(one='Nick', two='Tom', tree='Ann')
