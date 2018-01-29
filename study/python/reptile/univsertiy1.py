import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r= requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html,'lxml')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    pass

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^20}\t{2:^10}"
    print(tplt.format("排名","学校","成绩",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    print("Suc"+str(num))

def main():
    uinfo= []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,num=20)

main()