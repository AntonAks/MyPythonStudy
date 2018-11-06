import os
from datetime import datetime
import json
import shutil
import logging


# Logging config
log_filename = 'log_back_up.txt'
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d.%m.%y %H:%M:%S')
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(fh)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
log.addHandler(ch)


try:
    log.info('Started' + datetime.now().strftime("%c") + '\n')
    log.info('Read config file')
    with open('config.json') as json_data_file:
        config_data = json.load(json_data_file)

    source_path = config_data['config']['source']
    destination_path = config_data['config']['destination']

    json_data_file.close()

    log.info(f'source_path: {source_path}')
    log.info(f'destination_path: {destination_path}' + '\n')

    snapshot_folder_name = '\\back_up_' \
                           + str(datetime.today().year) \
                           + "_" + str(datetime.today().month) \
                           + "_" + str(datetime.today().day) \
                           + " " + str(datetime.today().hour) \
                           + "_" + str(datetime.today().minute) \
                           + "_" + str(datetime.today().second)

    log.info('Checking & create backup folder')
    if not os.path.isdir(destination_path):
        os.mkdir(destination_path)

    if not os.path.isdir(source_path):
        log.error('SOURCE DIRECTORY - NotADirectoryError: Directory is not exist')
        log.error('Try to check path for source and destination...')
        raise FileNotFoundError

    log.info('Copying')
    shutil.copytree(source_path, destination_path + snapshot_folder_name)
    log.info('Finished' + '\n')
except Exception as e:
    log.error(e.__str__())
