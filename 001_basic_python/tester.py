import datetime


string = datetime.datetime.now().strftime('%Y-%m-%d')

result_file_prefix = 'TaskResult_'
task_file_prefix = 'Task_'

r_list = ['TaskResult_b8bcc602-953e-4317-97ad-b0ab1776ad0b.xml',
          'TaskResult_197ebd5f-6080-4656-8950-ff451f3c0f22.xml',
          'TaskResult_0233d925-1481-46fb-b463-04beedd689f1.xml']


t_list = ['Task_b8bcc602-953e-4317-97ad-b0ab1776ad0b.xml',
          'Task_197ebd5f-6080-4656-8950-ff451f3c0f22.xml',
          'Task_0233d925-1481-46fb-b463-04beedd689f1.xml']


for r in r_list:
    for t in t_list:
        if r.replace(result_file_prefix, '') == t.replace(task_file_prefix, ''):
            print(r)




