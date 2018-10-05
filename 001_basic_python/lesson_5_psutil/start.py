import psutil
from fnmatch import fnmatch


print(psutil.virtual_memory())
exit()
print(list(psutil.virtual_memory()))



print(psutil.disk_partitions())

print(psutil.disk_usage('C:\\'))
print(psutil.disk_usage('D:\\'))


# for i in psutil.net_connections():
#     print(i)


print(psutil.pids())


# print(psutil.process_iter())


for p in psutil.process_iter():
    if fnmatch(p.name(), '*chrome*'):
        print(p.ppid, p.ppid(), p.name())


# p = psutil.Process(13264)
# print(p.name())
# print(p.terminate())
