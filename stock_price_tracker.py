import requests
from bs4 import BeautifulSoup



def appleStockPriceTracker():

    url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml') 
    # print(soup)
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('Current price of Apple Stock: ' + price)


def amazonStockPriceTracker():

    url = 'https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml') 
    # print(soup)
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('Current price of Amazon Stock: ' + price)

def nikolaStockPriceTracker():

    url = 'https://finance.yahoo.com/quote/NKLA?p=NKLA&.tsrc=fin-srch'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml') 
    # print(soup)
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('Current price of Nikola Corporation Stock: ' + price)


count = 0

while (count < 10):
   appleStockPriceTracker()
   amazonStockPriceTracker()
   nikolaStockPriceTracker()
   count = count + 1