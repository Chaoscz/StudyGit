# coding：utf-8
import requests
import json, time

# 本节采用请求头直接采集
# url = 'https://www.toutiao.com/search_content/?offset=0&format=json&keyword=python&autoload=true&count=20&cur_tab=1'
# https://www.toutiao.com/search_content/?offset=20&format=json&keyword=python&autoload=true&count=20&cur_tab=1
# page = 8*20  最大到offset160


pkeywords = '''Python学习笔记
Python教程
Python开发
Python函数
Python
Python3
Python爬虫
Python基础
Python网络爬虫
Python基础教程
Python编程
Python实战
Python学习
Python公开课
python手机
python window
python类
python入门教程
python面试'''.split('\n')


# print(pkeywords)


def get_data(url):
    wbdata = requests.get(url).text
    data = json.loads(wbdata)
    news = data['data']
    for n in news:
        if 'title' in n:
            title = n['title']
            comments_count = n['comments_count']
            url = n['article_url']
            keyword = ''.join(n['keywords'].split(','))
            # print(url,'|',title,'|',keyword,'|',comments_count)
            line = url + '|' + title + '|' + keyword + '|' + str(comments_count) + '\n'
            print(line)
            f = open('keyds.txt', 'a', encoding='utf-8')  # TXT文本保存
            f.write(line)
            f.close()

if __name__ == '__main__':
    for kw in pkeywords:
        for i in range(9):
            url = 'https://www.toutiao.com/search_content/?offset=' + str(
                    i * 20) + '&format=json&keyword=' + kw + '&autoload=true&count=20&cur_tab=1'
            print(i, kw, url)
            try:
                get_data(url)
            except:
                print('爬虫掉坑里了，爬起来继续')
                pass