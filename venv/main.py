import requests
import json
import sys
import allCurrency,appUI

class MainApp():
    def __init__(self):
        self.getToken()
    def getToken(self):
        req = requests.post("https://www.pathofexile.com/oauth/token",
                            headers={'Content-Type': 'application/x-www-form-urlencoded',
                                     'User-Agent': 'OAuth grintekk/1.0.0 (contact: grintekk@gmail.com)'},
                            data={'client_id': 'grintekk', 'client_secret': 'AhJQkvpeMx93',
                                  'grant_type': 'client_credentials', 'scope': 'account:stashes'})
        data = req.json()
        auth_headers = {'Authorization': f'Bearer {data["access_token"]}',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'OAuth grintekk/1.0.0 (contact: grintekk@gmail.com)'}
        url = "https://api.pathofexile.com/stash/scourge"
        stash_list = requests.get(url, headers=auth_headers, data={}).json()
        id_stash = stash_list['stashes'][0]['id']
        url = url + '/' + id_stash
        self.items_list = requests.get(url, headers=auth_headers, data={}).json()
        with open('items.txt', 'w') as outfile:
            json.dump(self.items_list['stash'], outfile, indent=4)
    def save_info(self):
        with open('items.txt', 'w') as outfile:
            json.dump(self.items_list['stash'], outfile, indent=4)

def main():
    app = MainApp()
    appUI.main_window()
if __name__ == "__main__":
    main()
