import logging
import os
import subprocess
from datetime import datetime
from time import sleep
import time_count as ts
from stock_update_new import run_stock_update

UPDATE_FLAG = False
start = datetime.today()

# Log tuning
log_filename = 'C:\\Users\\Администратор\\PycharmProjects\\qlik_update\\log\\new_sales_log' \
               + str(datetime.today().year) \
               + "-" + str(datetime.today().month) \
               + "-" + str(datetime.today().day) \
               + " " + str(datetime.today().hour) \
               + "-" + str(datetime.today().minute) \
               + '.txt'
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

subprocess.Popen("TASKKILL /IM Qv.* /f", shell=True)
log.warning("KILL OLD PROCESS!")

# Get files-list from sales directory
dir_sales_path_str = "E:\QlikView\\06 Applications\\07 QVD DB\\SH\\"
files_names_sales = list(os.listdir(dir_sales_path_str))

# Get files-list with prefix "doc_details_"
temp_list = list()
for i in range(0, len(files_names_sales)):
    if files_names_sales[i].startswith('doc_details_'):
        temp_list.append(files_names_sales[i])

files_names_sales = temp_list  # Rewrite files-list

log.info("START UPDATING !")

iteration_out = 20
while iteration_out != 0:
    iteration_out = iteration_out - 1
    log.debug("Left iterations " + str(iteration_out))
    # Separate TT ID by update time - "not today" and 4 days early
    id_update_list = list()
    for i in range(0, len(files_names_sales)):
        path_time = os.path.getmtime(dir_sales_path_str + files_names_sales[i])
        path_size = os.path.getsize(dir_sales_path_str + files_names_sales[i])
        if 0 > ts.get_delta_modify_days(path_time) > -6 and path_size > 29000:
            id_tt = str(files_names_sales[i]).replace('doc_details_', '').replace('.qvd', '')
            id_update_list.append(id_tt)

    # CAP on testing time
    # id_update_list = ['634026']#, '530138', '584919', '584914', '584888', '584836', '585246', '584784', '584745', '593234', '593235', '627241', '431859']

    if '530138' in id_update_list:
        log.info("UPDATE UVK !")
        id_update_list.remove('530138')
        cmd = "\"C:\Program Files\QlikView\Qv.exe\" /r /vvBD_NAME=" + \
              '530138' + \
              " \"E:\\QlikView\\06 Applications\\06 QVD Creators\\QVD Creator Transactions_Totus_sh.qvw\""
        try:
            subprocess.Popen(cmd, shell=True, cwd="E:\jobs").wait(1800)
        except subprocess.TimeoutExpired:
            log.error('UVK TimeoutExpired !!!')
            pass

    # Create command list to update
    cmd_list = list()
    for i in range(0, len(id_update_list)):
        cmd = "\"C:\Program Files\QlikView\Qv.exe\" /r /vvBD_NAME=" + \
              id_update_list[i] + \
              " \"E:\\QlikView\\06 Applications\\06 QVD Creators\\QVD Creator Transactions_Totus_sh.qvw\""
        cmd_list.append(cmd)
    log.debug("Need to update: " + str(len(cmd_list)) + " files")

    if len(cmd_list) == 0:
        log.debug("No more files to update.")
        UPDATE_FLAG = True
        break

    log.debug("Create the first update partition")
    try:
        process_partition = list()
        for i in range(0, 20):  # 20
            process_partition.append(cmd_list.pop())
    except IndexError:
        for i in range(0, len(cmd_list)):
            process_partition.append(cmd_list.pop())

    log.debug("Start to update!")
    run_process = list()
    for i in range(0, len(process_partition)):
        run_process.append(subprocess.Popen(process_partition[i], shell=True, cwd="E:\jobs"))

    exception_flag = ''
    update_timeout = 0
    while True:
        check = []
        for i in range(0, len(run_process)):
            check.append(run_process[i].poll())
        log.info('In Buffer: ' + str(len(cmd_list)) +
                 ', In Progress: ' + str(check.count(None)) +
                 ', Finish: ' + str(check.count(0)) +
                 ', update_timeout: ' + str(update_timeout) + " in 30")

        if check.count(None) < 20:  # 20
            try:
                run_process.append(subprocess.Popen(cmd_list.pop(), shell=True, cwd="E:\jobs"))
            except IndexError:
                pass
        sleep(10)
        update_timeout = update_timeout + 1

        if check.count(None) == 0 and len(cmd_list) == 0:
            log.debug("Update is end")
            break

        if update_timeout >= 30:  # 5
            for i in range(0, len(run_process)):
                run_process[i].terminate()
                run_process[i].kill()
            break
    try:
        log.warning('Starting check process' + '\n' + str(cmd_list[len(cmd_list) - 1]))
        subprocess.Popen(cmd_list[len(cmd_list) - 1], shell=True, cwd="E:\jobs").wait(300)
    except subprocess.TimeoutExpired:
        log.error('Kill stuck process!!!')
        subprocess.Popen("TASKKILL /IM Qv.* /f", shell=True)
        sleep(30)
        print("sleep - 30 sec after process killing")
    except IndexError:
        pass
    print("sleep - 30 sec before next iteration")
    sleep(30)

if not UPDATE_FLAG:
    log.warning("The update was not fully")

files = list(os.listdir("E:\\jobs\\runs\\"))
for i in range(0, len(files)):
    os.remove("E:\\jobs\\runs\\" + str(files[i]))

try:
    subprocess.Popen("E:\\jobs\\RUN_TRANS_ANALIT_SH.cmd", shell=True, cwd="E:\jobs").wait(3600)
except subprocess.TimeoutExpired:
    log.warning("TimeoutExpired Exception raised! RUN_TRANS_ANALIT - update time more than 60 min")

log.info('Sales update is complete. Remain time is: ' + str(datetime.today() - start))

run_stock_update()
