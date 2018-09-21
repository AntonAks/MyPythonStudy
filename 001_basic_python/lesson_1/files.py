""" This study script dedicated to operations with files """

import os

main_path = os.getcwd()

file_name = str(input('Enter new file name please: '))
# condition for delete all txt files in current
if file_name == 'del':
    # creating list of files in current folder
    files = os.listdir(main_path)
    for i in files:
        # if file name includes '.txt' mask we will remove it
        if '.txt' in i:
            os.remove(main_path + '\\' + i)
    print('All .txt files was deleted')
    exit()

else:
    full_file_path = main_path + '\\' + file_name + '.txt'
    # creating file for write
    with open(full_file_path, 'w') as My_File:
        print('File {} created'.format(file_name))
        text = str(input('Enter some text here: '))
        My_File.write(text + '\n')
        pass
    pass


# open file for read
with open(full_file_path, 'r') as My_File:
    text = My_File.read()
    print('File read result: {}'.format(text))
    pass


# open file for append
My_File = open(full_file_path, 'a')

while True:
    text = str(input('Enter some text here for append (enter exit for finish): '))
    if text == 'exit':
        break
    My_File.write(text + '\n')

with open(full_file_path, 'r') as My_File:
    text = My_File.read()
    print('File read result: {}'.format(text))
    pass

My_File.close()
