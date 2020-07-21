
import datetime
import requests
from bs4 import BeautifulSoup


def tracker(url, name):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml') 
    # print(soup)
    # print(soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}))

    try:
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        print('Current price of ' + name + ' ' + price)

    except:
        print("skip")




while (True):
   tracker('https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch', "Apple")
   tracker('https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch', "Amazon")
   tracker('https://finance.yahoo.com/quote/NKLA?p=NKLA&.tsrc=fin-srch', "Nikola Corporation")
   tracker('https://finance.yahoo.com/quote/IMRN?p=IMRN&.tsrc=fin-srch', "Immuron Limited")
   tracker('https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch', "Tesla")
   tracker('https://finance.yahoo.com/quote/AZN?p=AZN&.tsrc=fin-srch', "AstraZeneca")
   tracker('https://finance.yahoo.com/quote/GC=F?p=GC=F', "Gold")
   tracker('https://finance.yahoo.com/quote/ACB', "Aurora Cannabis")




 


