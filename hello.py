import os,time
import json
from selenium import webdriver

cookies_file_path = 'cookies.json'
# selenium 模拟登陆并保存Cookies.

browser = webdriver.Chrome()
browser.get('http://shiguangxiaowu.cn/')
browser.maximize_window()
time.sleep(3)
a = browser.find_element_by_class_name("login-form-normal")
a.click()
input('请完成登录后点击回车')
cookies = browser.get_cookies()
browser.add_cookie()
#写入本地cookies
with open(cookies_file_path,'w') as f:
    f.write(json.dumps(cookies))
browser.close()

with open(cookies_file_path,'r') as f:
    listCookie = json.loads(f.read())
#cookies格式转换

cookies = {}
for cookie in listCookie:
    cookies[cookie['name']] = cookie['value']
