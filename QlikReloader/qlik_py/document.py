import subprocess
import pandas as pd
from time import sleep
import datetime


class Document:

    task_name = ''
    qmc_task_path = ''
    full_reload_flag = None
    full_reload_flag_current_day = None
    reload_status = ''
    start_time = ''
    edx_path = ''
    password = ''
    status = 'Sleep'
    message_temp = ''

    def __init__(self, qmc_task_path, task_name, password, full_reload_flag, full_reload_flag_current_day):
        self.qmc_task_path = qmc_task_path
        self.task_name = task_name
        self.full_reload_flag = full_reload_flag
        self.full_reload_flag_current_day = full_reload_flag_current_day
        self.password = ' -password=' + '"' + password + '"'

    def reload(self, edx_path):
        self.edx_path = edx_path + ' -task='
        full_task_path = '"' + self.qmc_task_path + '/' + self.task_name + '"'
        full_command_name = self.edx_path + full_task_path + self.password
        self.reload_status = subprocess.Popen(full_command_name)

    def get_reload_status(self):
        return self.reload_status.poll()


def get_tasks_list(file_path):

    config_data = pd.read_csv(file_path)
    data_list = config_data.get_values()

    qmc_task_path_list = list(config_data['qmc_task_path'])
    task_name_list = list(config_data['task_name'])
    password_list = list(config_data['password'])
    full_reload_flag_list = list(config_data['full_reload_flag'])
    full_reload_flag_current_day_list = list(config_data['full_reload_flag_current_day'])

    list_of_qv_documents = []
    for i in range(0, len(data_list)):
        list_of_qv_documents.append(Document(qmc_task_path=qmc_task_path_list[i]
                                             , task_name=task_name_list[i]
                                             , password=password_list[i]
                                             , full_reload_flag=full_reload_flag_list[i]
                                             , full_reload_flag_current_day=full_reload_flag_current_day_list[i]))
    return list_of_qv_documents
