import json
import requests
import os

with open('items.json') as outfile:
    dataItems = json.load(outfile)

all_currency = []
#dataItems = dataItems['stash']
location = os.path.abspath("C:/Users/Admin/PycharmProjects/PoE_StashChecking/venv/Icons/")
for i in dataItems['items']:
    img_data = requests.get(i['icon']).content

    with open( location + '\\' +str(i['typeLine'])+'.png', 'wb') as handler:
        handler.write(img_data)
    #all_currency[count] = [i['stackSize'],i['typeLine']]
    #if i.get('stackSize'):
    #    all_currency.append([i['typeLine'],i['stackSize']])

print(all_currency)