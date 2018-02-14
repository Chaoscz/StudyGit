# coding = utf-8
import requests
import re
headers = {
    'Host': 'ss1.bdstatic.com',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
   'Referer': 'https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%20%E8%BF%90%E6%B2%B3%20%E4%BA%AC%E6%9D%AD&pn=0&oq=%E5%8C%97%E4%BA%AC%20%E8%BF%90%E6%B2%B3%20%E4%BA%AC%E6%9D%AD',
    'Connection': 'keep-alive'
}
base_url = 'https://www.baidu.com/'
s = requests.session()
s.get(base_url)
find_urls = []
for i in range(20):
    print(i)
    url = 'https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%20%E8%BF%90%E6%B2%B3%20%E4%BA%AC%E6%9D%AD&pn=' + str(
        i * 10)  # 关键词（北京 运河 京杭）
    print(url)
    content = s.get(url, headers=headers).text
    find_urls.append(content)
find_urls = list(set(find_urls))
f = open('url.txt', 'a+',encoding='utf-8')
f.writelines(find_urls)
f.close()

# coding = utf-8
import re
f = open('url.txt',encoding='utf-8').read()
f2 = open('urlin.txt', 'a+',encoding='utf-8')
find_urls = re.findall('href="http://www.baidu.com/link(.+?)"', f )
find_urls = list(set(find_urls))
find_u = []
for url_i in find_urls:
    in_url = 'http://www.baidu.com/link' + url_i + '\n'
    f2.write(in_url)
f2.close()

# 导入可能用到的库
import requests, json, re, random, csv, time, os, sys, datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = DesiredCapabilities.PHANTOMJS
dcap[ "phantomjs.page.settings.userAgent"] = "Mozilla / 4.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/51.0.2704.79 Safari/ 537.36Edge/14.14393"
# 请求头不一样，适应的窗口不一样！

driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.set_page_load_timeout(10)
driver.set_script_timeout(10)#这两种设置都进行才有效

find_urls = open('urlin.txt',encoding='utf-8').readlines()
# print(len(find_urls))  # 634个URL # 关键词（北京 运河 京杭）
i = 0
f = open('jh_text.txt', 'a+',encoding='utf-8')
for inurl in find_urls:
    print(i,inurl)
    i+=1
    try:
        driver.get(inurl)
        content = driver.page_source
        # print(content)
        soup = BeautifulSoup(content, "lxml")
        f.write(soup.get_text())
        time.sleep(1)
    except:
        driver.execute_script('爬虫跳坑里，等会继续')