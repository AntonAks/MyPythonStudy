""" This study script dedicated to LOGGING """

import os
import logging
import time

log_folder = '\\logging_files\\'
log_file = 'log.txt'

# Logging config:
log_filename = str(os.getcwd() + log_folder + log_file)
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

# Log Examples
logging.debug('Hello World!')
time.sleep(3)

logging.error('This is an error!')
time.sleep(6)

logging.info('This is a some information!')


