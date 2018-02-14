from selenium import webdriver #导入python版的selenium(webdriver)
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
'''
基于PhantomJS创建一个无界面浏览器，并且设置一下用户代理，
否则可能出现界面不兼容的情况
'''
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 5.5; windows NT)" )
browser = webdriver.PhantomJS(desired_capabilities=dcap)
'''
我们通过PhantomJS打开相关动漫网页，将相关动漫图片地址触发出来
'''
browser.get('http://ac.qq.com/ComicView/index/id/539443/cid/1')
print(browser.title) #获取标题<title>《宛香》遇见（1）-在线漫画-腾讯动漫官方网站</title>
print(browser.page_source) #打印当前网页所有源代码