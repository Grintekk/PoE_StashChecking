import json
import sys
import requests
import os

with open('items.txt') as outfile:
    #dataItems = json.load(outfile)
    dataItems = json.load(outfile)
location = os.path.abspath("C:/Users/Admin/PycharmProjects/PoE_StashChecking/venv/Icons/")

def getCurrency():
    all_currency = {}
    for i in dataItems['items']:
        if i.get('stackSize'):
            all_currency[i['typeLine']] = i['stackSize']
    return all_currency
def saveImg():
    for i in dataItems['items']:
        img_data = requests.get(i['icon']).content
        with open(location + '\\' + str(i['typeLine']) + '.png', 'wb') as handler:
            handler.write(img_data)
