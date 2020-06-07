import json 
import requests


api_url1 = 'http://IP:端口/get_group_member_list'
data1 = {
		'group_id': "群号",
		'no_cache': False
	}
rp = requests.post(api_url1,data=data1)
list_dx = json.loads(rp.text)
#print rp.text

dict_list = []
for list_a in list_dx['data']:
  qq_id = list_a['user_id']
  data2 = {
		'user_id' : qq_id,
                'status_id' : '0'
	  }
  dict_list.append(data2)
with open('./dx.json','w') as r:
  json.dump(dict_list,r)
