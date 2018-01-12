import requests

req = requests
kv = {'user-agent':'Mozilla/5.0'}
url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
r= req.get(url,headers= kv)
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
#print(r.text)