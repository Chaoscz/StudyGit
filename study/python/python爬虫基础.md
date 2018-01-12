# requests

```python
#requests的方法
import requests
requests.get()
requests.post()
requests.delete()
requests.head()
requests.options()
requests.patch()
requests.put()
```

```python
import requests
#请求百度
response = requests.get('https://www.baidu.com')
response.status_code #Http请求返回状态 200
response.text #http响应的内容 
response.encoding #从http header中获取的编码格式 ISO-8859-1
response.apparent_encoding #从内容中分析获得编码法格式  UTF-8
response.content #二进制形式
#异常
requests.ConnectionError #网络连接异常
requests.HTTPError 	#http 异常
requests.URLRequired #URL缺失异常
requests.TooManyRedirects #超过最大重定向次数，重定向异常
requests.ConnectTimeout #连接远程服务器超时
requests.Timeout #请求URL超时
requests.raise_for_status() #请求返回不是200,就抛出requests.HTTPError

```

```python
#爬去网页的通用代码框架
import requests
req = requests
def getHtmlText(url):
    try:
      resp = req.get(url,timeout=30)
      resp.raise_for_status()
      resp.encoding = resp.apparent_encoding
      return resp.text
    except:
      return '产生异常了'

if __name__ == "__main__":
    url = 'https://www.baidu.com'
    print(getHtmlText(url)) 
```
