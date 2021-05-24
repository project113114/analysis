import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup

def live_stock(stock):
    url = "https://in.finance.yahoo.com/quote/" + str(stock)
    r = requests.get(url)
    web_c = BeautifulSoup(r.text,'lxml')
    
    web_c = web_c.find('div',{"class":"D(ib) Mend(20px)" })
    web_c = web_c.find('span').text
    if web_c ==[]:
        web_c = "9999"
    return web_c

liststock =["%5ENSEI?p=%5ENSEI","%5EBSESN?p=%5EBSESN","EURINR%3DX?p=EURINR%3DX","INR%3DX?p=INR%3DX"]


for step in range(1,1001):
    price =list()
    col = list()
    times = datetime.datetime.now()
    times = times.strftime("%Y-%m-%d %H:%M:%S")
    for stock in liststock:
        price.append(live_stock(stock))
    col = [times]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('data.csv', mode="a", header=False)
    print(col)
