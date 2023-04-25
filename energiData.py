import json
import requests
from datetime import datetime, timedelta


class ElPrice():
    def __init__(self):
        self.ToDate = datetime.now().strftime("%Y-%m-%d")
        self.FromDate = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        self.PriceArea = "DK2"

    def get_data(self):
        url = "https://api.energidataservice.dk/dataset/Elspotprices?start=" + self.FromDate + "&end=" + self.ToDate + "&filter=%7B%22PriceArea%22%3A%20%22" + self.PriceArea + "%22%7D"
        print(url)
        response = requests.get(url)
        data = response.json()
        return data

    def save_data(self):
        data = self.get_data()
        with open('elprice.json', 'w') as outfile:
            json.dump(data, outfile)   

class EnergyMap():
    def __init__(self):
        self.ToDate = datetime.now().strftime("%Y-%m-%d")
        self.FromDate = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        self.PriceArea = "DK2"

    def get_data(self):
        url = 'https://api-access.electricitymaps.com/2w97h07rvxvuaa1g/power-breakdown/history?zone=DK-DK2'
        headers = {"X-BLOBR-KEY": "WSnT5dZ6KZqODpVVdJruZshULzomfCg3"}  
        print(url)
        response = requests.get(url, headers=headers)
        data = response.json()
        return data    
    
    def make_Pb_Dk2(self):
        data = self.get_data()
        with open('PBDK2.json', 'w') as outfile:
            json.dump(data, outfile) 

    def make_PB_Zone(self):  
        url = 'https://api.electricitymap.org/v3/zones'
        #headers = {"X-BLOBR-KEY": "WSnT5dZ6KZqODpVVdJruZshULzomfCg3"}   
        response = requests.get(url)
        data = response.json()
        with open('PB_Zone.json', 'w') as outfile:
            json.dump(data, outfile)      

if __name__ == '__main__':
    #EG = ElPrice()
    #data = EG.get_data()
    #EG.save_data()
    #print(data)
    EM = EnergyMap()
    #data = EM.get_data()
    #print(data)
    #EM.make_Pb_Dk2()
    EM.make_PB_Zone()
