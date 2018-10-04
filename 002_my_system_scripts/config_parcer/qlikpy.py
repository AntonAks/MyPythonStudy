import subprocess
from time import sleep
import datetime


class Document:

    task_name = ''
    qmc_task_path = ''
    reload_status = ''
    start_time = ''
    edx_path = ''
    password = ''
    status = 'Sleep'
    message_temp = ''

    def __init__(self, qmc_task_path, task_name, password):
        self.qmc_task_path = qmc_task_path
        self.task_name = task_name
        self.password = ' -password=' + '"' + password + '"'

    def reload(self, edx_path):
        self.edx_path = edx_path + ' -task='
        full_task_path = '"' + self.qmc_task_path + '/' + self.task_name + '"'
        full_command_name = self.edx_path + full_task_path + self.password
        self.reload_status = subprocess.Popen(full_command_name)

    def get_reload_status(self):
        return self.reload_status.poll()
