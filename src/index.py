#This will be the main file

import bs4
import requests
from bs4 import BeautifulSoup

def getPrice():
    r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup = bs4.BeautifulSoup(r.text, "xml")
    price = soup.find_all("div")
    print(price)

#, {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

    return price 