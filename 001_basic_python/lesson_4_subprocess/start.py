import subprocess
import threading
import sys

from time import sleep

subprocess.Popen("C:\\Users\\Anton Aksynov\\Documents\\GitRepo\\MyPythonStudy\\001_basic_python\\lesson_4_subprocess\\p_1.cmd")
subprocess.Popen("C:\\Users\\Anton Aksynov\\Documents\\GitRepo\\MyPythonStudy\\001_basic_python\\lesson_4_subprocess\\p_2.cmd")



# init events
e1 = threading.Event()
e2 = threading.Event()

# init threads
t1 = threading.Thread(target=writer, args=(0, e1, e2))
t2 = threading.Thread(target=writer, args=(1, e2, e1))






