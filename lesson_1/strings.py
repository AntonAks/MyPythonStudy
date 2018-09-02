""" This study script dedicated to work with strings """

my_string = 'I believe whatever does not kill you simply makes you… stranger.'
print(my_string)

# cut
print('my_string[0:9]: {}'.format(my_string[0:9]))
print('my_string[19:32]: {}'.format(my_string[19:32]))
print('my_string[19:]: {}'.format(my_string[19:]))
print('my_string[0:-9]: {}'.format(my_string[0:-9]))

# replace
my_string_2 = my_string.replace('I believe', 'I am sure that')
print('my_string.replace(): {}'.format(my_string_2))

# split
my_strings_list = my_string.split(' ')
print(my_strings_list)

# find
find = my_string.find('kill')
print('my_string.find("kill"): {}'.format(find))

# 'in' statement
print('kill' in my_string)
print('live' in my_string)
print('Hello world' not in my_string)
