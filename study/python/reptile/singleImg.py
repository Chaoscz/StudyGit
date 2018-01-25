import requests
import  os

root = "D://img//"
url = "http://img0.dili360.com/rw14/ga/M01/03/9B/wKgBy1RRn8WAdFphAAYDw4yM3BE483.jpg";
path = root + url.split("/")[-1]
try:
    if not os.path.exists(path):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("保存成功")
    else:
        print("该文件已经存在")
except:
    print("爬取失败")
