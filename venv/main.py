import requests
import json


req = requests.post("https://www.pathofexile.com/oauth/token", headers= {'Content-Type':'application/x-www-form-urlencoded','User-Agent': 'OAuth grintekk/1.0.0 (contact: grintekk@gmail.com)'},
              data={'client_id' : 'grintekk', 'client_secret' : 'AhJQkvpeMx93', 'grant_type' :'client_credentials' , 'scope' : 'account:stashes'})
data = req.json()
auth_headers = {'Authorization':f'Bearer {data["access_token"]}','Content-Type':'application/x-www-form-urlencoded','User-Agent': 'OAuth grintekk/1.0.0 (contact: grintekk@gmail.com)'}
url = "https://api.pathofexile.com/stash/scourge"
stash_list = requests.get(url , headers=auth_headers, data={}).json()
id_stash = []
for i in stash_list['stashes']:
    id_stash.append(i['id'])
url = url + '/' +  id_stash[0]
items_list = requests.get(url, headers=auth_headers, data={}).json()
print(url)
with open('items.json','w') as outfile:
    json.dump(items_list['stash'],outfile,indent=4)
#with open('stash_id.json') as outfile:
#    new = json.load(outfile)
#for i in new:
#    print(i)
#all_currency = {}
#for i in items_list[['stash']:'items']:
#    all_currency[i['typeLine']] = i['stackSize']
