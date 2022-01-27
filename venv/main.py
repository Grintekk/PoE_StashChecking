import requests
import json
import sys
import os

class MainApp():
    def __init__(self):
        self.getToken()
    def getToken(self): #получаем токен и формируем ссылку на запрос
        req = requests.post("https://www.pathofexile.com/oauth/token",
                            headers={'Content-Type': 'application/x-www-form-urlencoded',
                                     'User-Agent': 'OAuth grintekk/1.0.0 (contact: grintekk@gmail.com)'},
                            data={'client_id': 'grintekk', 'client_secret': 'AhJQkvpeMx93',
                                  'grant_type': 'client_credentials', 'scope': 'account:stashes'})
        data = req.json()
        self.auth_headers = {'Authorization': f'Bearer {data["access_token"]}',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'OAuth grintekk/1.0.0 (contact: grintekk@gmail.com)'}
        self.url = "https://api.pathofexile.com/stash/scourge"
        stash_list = requests.get(self.url, headers=self.auth_headers, data={}).json()
        id_stash = stash_list['stashes'][0]['id']
        self.url = self.url + '/' + id_stash
        self.items_list = self.send_request()
        self.save_file(self.items_list,"New_info")
        self.save_file(self.ninja_request(),"Currency_Equivalent")

    def send_request(self): #обновляем инфу запросом
        items_list = requests.get(self.url, headers=self.auth_headers, data={}).json()
        items_list = items_list['stash']
        items_list = self.give_value(items_list)
        return items_list
    def give_value(self,items_list): #возвращает словарь валютки избавляясь от лишнего
        all_currency ={}
        for i in items_list['items']:
            if i.get('stackSize'):
                all_currency[i['typeLine']] = i['stackSize']
        return all_currency
    def save_file(self,all_currency, file_name):
        with open(str(file_name) + '.txt', 'w') as outfile:
            json.dump(all_currency, outfile, indent=4)
    def open_file(self, file_name):
        with open(str(file_name)+'.txt') as outfile:
            data_items = json.load(outfile)
        return data_items
    def ninja_request(self):
        req = requests.get("https://poe.ninja/api/data/currencyoverview?type=Currency&league=Standard")
        data = req.json()
        currency_list = {}
        for i in data["lines"]:
            currency_list[i["currencyTypeName"]] = i["chaosEquivalent"]
        return currency_list
    # def getCurrency(self,file_name):# из выбраного файл список валюты
    #     data_items = self.open_file(file_name)
    #     # all_currency = {}
    #     # for i in data_items['items']:
    #     #     if i.get('stackSize'):
    #     #         all_currency[i['typeLine']] = i['stackSize']
    #     return all_currency

    def saveImg(self):
        data_items = self.open_file("items")
        location = os.path.abspath("C:/Users/Admin/PycharmProjects/PoE_StashChecking/venv/Icons/")
        for i in data_items['items']:
            img_data = requests.get(i['icon']).content
            with open(location + '\\' + str(i['typeLine']) + '.png', 'wb') as handler:
                handler.write(img_data)
###
# def main():
#     app = MainApp()
#     app.give_new_value()
#     appUI.main_window()
# #if __name__ == "__main__":
# main()
