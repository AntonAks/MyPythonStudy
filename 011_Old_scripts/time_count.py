import datetime
import time


def get_delta_modify_days(path_getmtime):
    file_modify_date = datetime.date(year=time.localtime(path_getmtime)[0], month=time.localtime(path_getmtime)[1], day=time.localtime(path_getmtime)[2])
    today = datetime.date.today()
    check_str = str(file_modify_date - today)
    if check_str == '0:00:00':
        check_int = 0
    else:
        check_int = int(check_str.split()[0])

    return check_int
