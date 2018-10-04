from qlik_py.document import Document, get_tasks_list
from time import sleep
import datetime
import threading
import pandas

file_path = 'D:\\SystemBatches\\Python script\\QlikReloader\\qlik_py\\config_for_qlik_preloader.csv'

list_of_docs = get_tasks_list(file_path)

# list_of_docs = list_of_docs[2:5]


edx = 'D:\QlikAnalyzer\EDX_COM\QMSEDX.exe'

for i in range(0, len(list_of_docs)):
    list_of_docs[i].reload(edx_path=edx)


while True:
    check_list = []
    for i in list_of_docs:
        check_list.append(i.get_reload_status())
    print(check_list)
    if check_list.count(None) == 0:
        break
    sleep(1)

print('Reload finished')
