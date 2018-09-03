# recursive function (factorial)
def my_factorial_function(n):
    if n == 0:
        return 1
    else:
        return n * my_factorial_function(n - 1)


print(f"factorial result: {my_factorial_function(10)}")


# simple sort function
def my_sort_function(sequence):
    if type(sequence) is str:
        print('this is string')
        sequence = list(sequence)
        for j in range(0, len(sequence)):
            for i in range(0, len(sequence) - 1):
                if sequence[i] > sequence[i + 1]:
                    x = sequence[i + 1]
                    sequence[i + 1] = sequence[i]
                    sequence[i] = x
        return sequence
    if type(sequence) is list:
        print('this is list')
        for j in range(0, len(sequence)):
            for i in range(0, len(sequence) - 1):
                if sequence[i] > sequence[i + 1]:
                    x = sequence[i + 1]
                    sequence[i + 1] = sequence[i]
                    sequence[i] = x
        return sequence
    else:
        raise TypeError('Function must take string or list argument')


result = my_sort_function('Hello World Brother!')
print(result)
result = my_sort_function([9, 3, 34, 75, 12, 7, 23, 1, 6, 52])
print(result)


# simple example
def my_function(a, b):
    # Returns 5% of the sum a & b
    return sum((a, b)) * 0.05


print(f"1. simple example result is: {my_function(30, 50)}")


# example with *args
def my_function_2(*args):
    return sum(args) * 0.05


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
