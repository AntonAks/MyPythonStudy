import pandas as pd
import os


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

file_path = 'C:\\Users\\Anton Aksynov\\Documents\\GitRepo\\MyPythonStudy\\002_my_system_scripts\\config_parcer\\config_for_qlik_preloader.csv'

config_data = pd.read_csv(file_path)
column_names = list(config_data.columns)

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


for i in list_of_qv_documents:
    print(i.task_name, i.qmc_task_path)

