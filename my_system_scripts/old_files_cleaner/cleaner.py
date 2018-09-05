""" This simple script serves for remove old files to windows trash """

import datetime
import time
import os
from fnmatch import fnmatch
from send2trash import send2trash
import logging


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


# Read properties for clearing
with open(os.getcwd() + '\\' + 'config_mask_time.txt', 'r') as ins:
    properties = []
    for line in ins:
        if 'INFO:' in line:
            continue
        properties.append(line)

# mask for clearing files
files_mask = properties[0]
log.info(files_mask)
files_mask = files_mask.replace('MASK: ', '').strip()

# age of files
hours_old = properties[1]
log.info(hours_old)
hours_old = hours_old.replace('HOURS: ', '')


# Read folders for clearing
with open(os.getcwd() + '\\' + 'config_path.txt', 'r') as ins:
    folders_form_config = []
    for line in ins:
        if 'INFO:' in line:
            continue
        folders_form_config.append(line.strip())
dirs = folders_form_config


log.info("START CLEARING")


remove_files_list = list()


for dir_path in dirs:
    log.info(str('SEARCHING FOR OLD LOG ' + dir_path))
    for path, subdirs, files in os.walk(dir_path):
        for name in files:
            if fnmatch(name, files_mask):
                file_path = str(path + '\\' + name)
                file_time = os.path.getmtime(file_path)
                file_days_old = datetime.datetime.fromtimestamp(time.time()) - datetime.datetime.fromtimestamp(
                    file_time)
                if file_days_old > datetime.timedelta(hours=int(hours_old)):
                    remove_files_list.append(file_path)

    for j in range(0, len(remove_files_list)):
        send2trash(remove_files_list[j])
        # log.info(remove_files_list[j] + ' REMOVED TO TRASH')

log.info(f"Removed: {len(remove_files_list)} {files_mask} files")
log.info("FINISHED")
