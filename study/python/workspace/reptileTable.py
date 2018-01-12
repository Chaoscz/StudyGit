# coding:utf-8
import requests,csv
from bs4 import BeautifulSoup

headers = {
    # 'Host': 'Wx:nemoon',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}  # 请求头，蛇无头不行，带上吧，后面会讲到用Cookie实现单账号免密登录

# 下期预告：
# 1，在请求前Host，Referer，Cookies以字典的形式直接定义
# 2，直接在请求前设置Cookies
    # s.cookies.set('mycookie','value') #设置cookies
# 3, 在请求过程中更新Cookies
    # c = requests.cookies.RequestsCookieJar()#定义一个cookie对象
    # c.set('cookie-name', 'cookie-value')#增加cookie的值
    # s.cookies.update(c)#更新s的cookie
# 4，删除Cookies
    # s.cookies.clear()#删除cookies,也可以使用s.cookies=None的方式将所有cookies删除

s = requests.session()  # 保留会话


def bs_test(text):
    soup = BeautifulSoup(text, "lxml")
    table_trs = soup.find_all('tr',{'class':'hover'})
    # 预留小作业，提取表头，并写入csv
    for i in table_trs:
        content=[ i_in.text for i_in  in i.find_all('td')]
        print(content)
        with open('file_name.csv', 'a', newline='') as f:  # 删除空格
            f_csv = csv.writer(f)
            f_csv.writerow(content)
            f.close()


if __name__ == '__main__':
    # base_url = 'http://www.jxyycg.cn/yzxt/publicity/view?id=eb1a21f2ab6a40119544e9048417bc1f&pageNo=2'
    for i in range(1) : # 用1页测试一下
        url = 'http://www.jxyycg.cn/yzxt/publicity/view?id=eb1a21f2ab6a40119544e9048417bc1f&pageNo=' +str(i+1)
        req_text = s.get(url).text
        # print(req_text) #  BS
        urls = bs_test(req_text)