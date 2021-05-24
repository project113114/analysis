import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup
url = 'https://socialblade.com/youtube/user/addicteda1/realtime'
r =requests.get(url)
web_c = BeautifulSoup(r.text, "lxml")
web_c = web_c.find('div',{'class':'odometer-inside'})
web_c = web_c.find('snap')
print(web_c)
# <div class="counterdescyoutube">on YouTube</div> 