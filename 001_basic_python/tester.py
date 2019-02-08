import pytz
import time
import datetime
from os import path

file_full_path_1 = 'C:\\Users\\Anton Aksynov\\Desktop\\StateReader Distribution\\2018-01-02_STA_DE16370400440504848300_EUR_000001.txt'
file_full_path_2 = 'C:\\Users\\Anton Aksynov\\Desktop\\StateReader Distribution\\test_tab.qvd'

m_time_1 = datetime.datetime.fromtimestamp(path.getmtime(file_full_path_1))
m_time_2 = datetime.datetime.fromtimestamp(path.getmtime(file_full_path_2))

print(m_time_1, m_time_1.timetuple())
print(m_time_2, m_time_2.timetuple())

exit()


