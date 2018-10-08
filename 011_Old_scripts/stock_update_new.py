import os
import subprocess
import time_count as ts
from datetime import datetime
from time import sleep
import logging


def run_stock_update():
    # Log tuning
    log_filename = 'C:\\Users\\Администратор\\PycharmProjects\\qlik_update\\log\\new_stock_log' \
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

    # Get files-list from stock directory
    dir_stock_path_str = "E:\QlikView\\06 Applications\\09 Inventory\FilialStocks\SH\\"
    files_names_stock = list(os.listdir(dir_stock_path_str))

    # Get files-list with prefix "doc_details_"
    temp_list = list()
    for i in range(0, len(files_names_stock)):
        if files_names_stock[i].startswith('Stocks_'):
            temp_list.append(files_names_stock[i])

    files_names_stock = temp_list  # Rewrite files-list

    iteration_out = 10
    while iteration_out != 0:
        iteration_out = iteration_out - 1
        log.debug("Left iterations " + str(iteration_out))
        # Separate TT ID by update time - "not today"
        id_update_list = list()
        for i in range(0, len(files_names_stock)):
            path_time = os.path.getmtime(dir_stock_path_str + files_names_stock[i])
            path_size = os.path.getsize(dir_stock_path_str + files_names_stock[i])
            if 0 > ts.get_delta_modify_days(path_time) > -6 and path_size > 15500:
                id_tt = str(files_names_stock[i]).replace('Stocks_', '').replace('.qvd', '')
                id_update_list.append(id_tt)

        # CAP on testing time
        # id_update_list = ['584835', '583667', '584935', '584919', '584914', '584888', '584836', '585246']
        # id_update_list = ['585245', '585235', '634026', '584919', '634388']
        # Create command list to update
        cmd_list = list()
        for i in range(0, len(id_update_list)):
            cmd = "\"C:\Program Files\QlikView\Qv.exe\" /r /vvFilialsList=" + \
                  id_update_list[i] + \
                  " \"E:\\QlikView\\06 Applications\\09 Inventory\\CreateQVDFilialStocs_TOTUS_sh.qvw\""

            cmd_list.append(cmd)
        log.debug("Need to update: " + str(len(cmd_list)) + " files")

        if len(cmd_list) == 0:
            log.debug("No more files to update.")
            break

        log.debug("Create the first update partition")
        try:
            process_partition = list()
            for i in range(0, 20):
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
                     ', update_timeout: ' + str(update_timeout) + " in 120" +
                     ', ' + exception_flag)

            if check.count(None) < 10:
                try:
                    run_process.append(subprocess.Popen(cmd_list.pop(), shell=True, cwd="E:\jobs"))
                except IndexError:
                    exception_flag = 'Buffer is over'
            sleep(5)
            update_timeout = update_timeout + 1

            if check.count(None) == 0 and len(cmd_list) == 0:
                log.debug("Update is end")
                break

            if update_timeout >= 120:
                for i in range(0, len(run_process)):
                    run_process[i].terminate()
                    run_process[i].kill()
                break
        print("sleep - 30 sec")
        sleep(30)

    full_stock_update = subprocess.Popen("E:\\QlikView\\06 Applications\\09 Inventory\\CreateQVDStocs_sh.cmd", shell=True).wait(3600)
    log.debug("STOCK UPDATE IS END")


# run_stock_update()