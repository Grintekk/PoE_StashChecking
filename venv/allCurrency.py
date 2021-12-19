import json

with open('items.json') as outfile:
    dataItems = json.load(outfile)

all_currency = []
#dataItems = dataItems['stash']
count = 0
for i in dataItems['items']:
    #all_currency[count] = [i['stackSize'],i['typeLine']]
    if i.get('stackSize'):
        all_currency.append([i['typeLine'],i['stackSize']])
print(all_currency)