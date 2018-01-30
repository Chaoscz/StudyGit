import  requests
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def parseHtml(glt,html):
    soup = BeautifulSoup(html,"lxml")
    print(soup.prettify())

def printData(glt):
    pass


if __name__ == '__main__':
    keyword = '书包'
    depth = 0
    start_url = "https://s.taobao.com/search?q="+keyword
    goodsInfo = []

    for i in range(depth):
        try:
            url = start_url + "&s="+str(44*i)
            html = getHtmlText(url)
            parseHtml(goodsInfo,html)
            printData(goodsInfo)
        except:
            continue
    printData(goodsInfo)




