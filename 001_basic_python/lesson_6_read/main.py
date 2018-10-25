import os
import re

print(os.getcwd())
full_file_path = os.getcwd() + '\\' + 'Settings_CFF.ini'

# Settings_CFF.ini
with open(full_file_path, 'r') as My_File:
    text = My_File.read()
    # print('File read result: {}'.format(text))
    pass


match = re.search('(vFirstXLoad[\D\d]{10})', text)

vFirstXLoad = re.findall('[01]', match.group())[0]

print(vFirstXLoad)
