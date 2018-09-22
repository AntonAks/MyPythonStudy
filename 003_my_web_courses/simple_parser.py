import requests
import datetime
from collections import Counter

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
user_id = 176356599
domain = "https://api.vk.com/method"
fields = 'bdate'

query = f"{domain}/friends.get?access_token={ACCESS_TOKEN}&user_id={user_id}&fields={fields}&v=5.71"
response = requests.get(query)

result = response.json()
result = result['response']
result = result['items']


temp_list_1 = []
temp_result = []
for i in range(0, len(result)):
    if 'bdate' in str(result[i]):
        # print(result[i]['bdate'])
        temp_list_1.append(result[i]['bdate'])


for i in range(0, len(temp_list_1)):
    if len(temp_list_1[i].split('.')) == 3:
        temp_result.append(datetime.datetime.now().year - int(temp_list_1[i].split('.')[2]))

final_result = list(Counter(temp_result).items())
final_result = sorted(final_result, key=lambda tup: tup[0], reverse=False)
final_result = sorted(final_result, key=lambda tup: tup[1], reverse=True)

print(final_result)
