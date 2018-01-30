#import urllib


#response = urllib.request.urlopen('http://localhost:8080/ibms')
#print response.read()

import requests
from bs4 import  BeautifulSoup

r = requests.get('https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E4%B9%A6%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=shubao&suggest_query=shubao&source=suggest&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=44')
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo,'lxml')
print(soup.prettify())