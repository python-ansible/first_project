from bs4 import BeautifulSoup
import requests

r = 'http://blog.csdn.net/huangxiongbiao/article/details/45584407'
url = requests.get(r)
print(url)
soup = BeautifulSoup(url.text,'lxml')
print(soup.get_text())