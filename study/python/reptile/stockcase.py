import requests
from bs4 import BeautifulSoup
import traceback
import re
def getHtmlText(url,code = 'utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def getStockList(lst,stockUrl):
    print('查找a标签\n')
    html = getHtmlText(stockUrl,"GB2312")
    soup = BeautifulSoup(html,'lxml')
    a = soup.find_all('a')
    print('a标签'+str(len(a))+"个")
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
        except:
            continue




def getStockInfo(lst,stockUrl,fpath):
    count = 0
    for stock in lst:
        url = stockUrl+stock +'.html'
        html = getHtmlText(url)
        try:
            if html == '':
                continue
            infoDict ={}
            soup = BeautifulSoup(html,'lxml')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({"股票名称":name.text.split()[0]})
            keyList = stockInfo.find_all("dt")
            valueList = stockInfo.find_all("dd")
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+"\n")
            count = count+1
            print("\r当前进度{:.2f}%".format(count*100/len(lst)),end="")
        except:
            count = count + 1
            print("\r当前进度{:.2f}%".format(count * 100 / len(lst)), end="")
            continue

if __name__ == '__main__':
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://stocklist.txt'
    slist = []
    print('开始爬虫:\n')
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)