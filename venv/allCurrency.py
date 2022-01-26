import json
import sys
import requests
import os

def open_file():
    with open('items.txt') as outfile:
        data_items = json.load(outfile)
    return data_items
def getCurrency():
    data_items = open_file()
    all_currency = {}
    for i in data_items['items']:
        if i.get('stackSize'):
            all_currency[i['typeLine']] = i['stackSize']
    return all_currency
def saveImg():
    data_items = open_file()
    location = os.path.abspath("C:/Users/Admin/PycharmProjects/PoE_StashChecking/venv/Icons/")
    for i in data_items['items']:
        img_data = requests.get(i['icon']).content
        with open(location + '\\' + str(i['typeLine']) + '.png', 'wb') as handler:
            handler.write(img_data)
