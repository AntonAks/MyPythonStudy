import os
from fnmatch import fnmatch
from send2trash import send2trash


root = 'G:\\QlikView Snapshot Data\\01 ODS\\'
files_extension_mask_list = ['*.*']
subfolder_mask_list = ['*\ZZ_OLD\*', '*\zz_Old\*', '*\zz_old\*']


files_for_delete = []

for mask_subfolder in subfolder_mask_list:
    for mask_file in files_extension_mask_list:
        for folder, subfolder, files in os.walk(root):
            if fnmatch(folder, mask_subfolder):
                for name in files:
                    full_file_path = str(folder + '\\' + name)
                    if fnmatch(full_file_path, mask_file):
                        files_for_delete.append(full_file_path)


with open('files_for_delete.txt', 'w') as file:
    file.truncate(0)
    for i in files_for_delete:
        file.write(i + ' size: ' + str(os.path.getsize(i)) + '\n')


for f in files_for_delete:
    send2trash(f)



# os.makedirs("C:\\Users\\Anton Aksynov\\Documents\\GitRepo\\MyPythonStudy\\111_test_python\\lesson_434_subprocess\\fgfgdfg")

