""" This simple script serves for remove old files to windows trash """
import datetime
import time
import os
import logging
from fnmatch import fnmatch
from send2trash import send2trash


def func_check_path_exist(file_folder_path):
    if not os.path.exists(file_folder_path):
        log.error(f"Cannot find file or folder - {file_folder_path}")
        exit()


# Logging config
log_filename = os.getcwd() + '\\log_cleaner.txt'
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(fh)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
log.addHandler(ch)


log.info('\n--- SCRIPT STARTED ---\n')


config_path_properties = os.getcwd() + '\\' + 'config_mask_time.txt'
config_path_folders = os.getcwd() + '\\' + 'config_path.txt'

# check for config files (exist or not)
func_check_path_exist(config_path_properties)
func_check_path_exist(config_path_folders)


# Read properties for clearing
with open(config_path_properties, 'r') as ins:
    properties = []
    for line in ins:
        if 'INFO:' in line:
            continue
        properties.append(line)

# mask for clearing files
files_mask = properties[0]
log.info(files_mask)
files_mask = files_mask.replace('MASK: ', '').strip()
files_mask = files_mask.split(',')

for i in range(0, len(files_mask)):
    files_mask[i] = files_mask[i].strip()


# age of files
hours_old = properties[1]
log.info(hours_old)
hours_old = hours_old.replace('HOURS: ', '')


# Read folders for clearing
with open(config_path_folders, 'r') as ins:
    folders_form_config = []
    for line in ins:
        if 'INFO:' in line:
            continue
        folders_form_config.append(line.strip())
        # check for folders (exist or not)
        func_check_path_exist(line.strip())
dirs = folders_form_config


log.info("START CLEARING")


remove_files_list = list()

for mask in files_mask:
    for dir_path in dirs:
        log.info(str(f"SEARCHING FOR OLD {mask} FILES" + dir_path))
        for path, subdirs, files in os.walk(dir_path):
            for name in files:
                if fnmatch(name, mask):
                    file_path = str(path + '\\' + name)
                    file_time = os.path.getmtime(file_path)
                    file_days_old = datetime.datetime.fromtimestamp(time.time()) - datetime.datetime.fromtimestamp(
                        file_time)
                    if file_days_old > datetime.timedelta(hours=int(hours_old)):
                        remove_files_list.append(file_path)
        for j in range(0, len(remove_files_list)):
            send2trash(remove_files_list[j])


log.info(f"Removed: {len(remove_files_list)} {files_mask} files")
log.info("FINISHED")
