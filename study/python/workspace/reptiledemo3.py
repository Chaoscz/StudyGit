# coding = utf-8

import requests
import re, json
from bs4 import BeautifulSoup
import time
headers = {
    'Host': 'www.toutiao.com',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Cookie': 'tt_webid=6468554118361204238; 。。。。不要随便让人看到你的小秘密',
    'Connection': 'keep-alive'
}

s = requests.session()


def post_data(base_url,post_content,post_id):
    try:
        # base_url = 'http://toutiao.com/group/64689424888533888/'
        url2 = 'http://www.toutiao.com/user/info/'
        content = s.get(url2, headers=headers) # 获取Useinfog，更新session
        # soup = BeautifulSoup(content, "lxml")
        # print(soup.prettify())
        headers['Referer'] = base_url
        url3 = 'http://www.toutiao.com/api/comment/post_comment/'
        data = {
            'status':post_content,
            'content': post_content,
            'group_id':post_id,
            'item_id':post_id

        }
        s.post(url3, headers=headers, data=data)  # 评论文章
        print('评论成功啦，嚯嚯')
    except:
        print('掉坑里了，爬起来')
        pass

f_lines = open('sorted.txt','r',encoding='utf-8').readlines()
posted_urls = open('posted.txt','r',encoding='utf-8').read()
# print(f_lines[0].strip().split(','))  # 实现记录已评论的Url，中断后可以接着评论
for f_line in  f_lines:
    if 'http://toutiao.com/group/' in f_line:  # 说明是可以评论的文章
        line_list = f_line.strip().split(',')
        base_url = line_list[1]
        print(base_url)
        post_content = '大神，你发的《'+ line_list[2]+'》很有借鉴意义，能否转发呢？'
        # print(post_content)
        post_id = base_url.split('/')[-2]
        if base_url  not in posted_urls :  # 进入下一个循环
            try:
                time.sleep(3)
                post_data(base_url,post_content,post_id)
                f_posted = open('posted.txt','a',encoding='utf-8')
                f_posted.write(base_url+'\n')
                f_posted.close()
            except:
                print('又他妈掉坑里了，爬起来')
                pass

        else:
            print('曾经评论过了')