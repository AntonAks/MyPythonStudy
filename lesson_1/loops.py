""" This study script dedicated to cycles and conditional operators """

# created list object
my_list = list()

# filling list object with FOR loop and range() function
for i in range(0, 20, 1):
    my_list.append(i)

# printing result
print("My first list: {list}".format(list=my_list))


# creating new list and filling it with even numbers from first list
my_list_even = list()
for i in my_list:
    if i % 2 == 0:
        my_list_even.append(i)

print("My even list: {list}".format(list=my_list_even))

# WHILE LOOP

# while with counter
i = 0
while i < len(my_list_even):
    print("While loop: {list}".format(list=my_list_even[i]))
    i = i + 1

# while with break statement=
while True:
    answer = str(input('Enter something (for exit enter - 0): '))
    if answer == '0':
        print('EXIT')
        break
    else:
        print('Your word is {answer}'.format(answer=answer))
