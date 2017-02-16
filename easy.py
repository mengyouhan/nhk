from bs4 import BeautifulSoup
import requests
import os,re,time
from selenium import webdriver

# PhantomJS
class GetNews():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def start(self,url):
        # driver = webdriver.Chrome()
        # url = 'http://www3.nhk.or.jp/news/easy/k10010861721000/k10010861721000.html'

        self.driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        select = "#newsarticle"
        y = soup.select(select)

        sa = re.sub(r"(<rt>.{1,14}</rt>)", '', str(y)[1:-1])
        soup2 = BeautifulSoup(sa, 'lxml')
        su = [x.get_text() for x in soup2][0].strip()
        print([x.get_text() for x in soup2])
        yuanwen = re.sub(r"\n", '', su)
        print(yuanwen)
        # print(type(la))
        return yuanwen


new = GetNews()
# url1 = 'http://www3.nhk.or.jp/news/easy/k10010861721000/k10010861721000.html'
url2 = 'http://www3.nhk.or.jp/news/easy/k10010876321000/k10010876321000.html'
new.start(url2)
# print(new.start(url1))
# print("_________________")
# print(new.start(url2))
http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/sortprefix:accent/narabi1:kata_asc/narabi2:accent_asc/narabi3:mola_asc/yure:visible/curve:fujisaki/details:invisible/limit:20/word:%E7%99%BA%E8%A1%A8%20%E8%A6%81%E9%A0%98%20%EF%BD%9E%E3%81%99%E3%82%8B%20%E5%AD%A6%E7%BF%92%20%E6%96%B0%E3%81%97%E3%81%84%20%E4%BD%BF%E3%81%86%20%E6%97%A5
http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/sortprefix:accent/narabi1:kata_asc/narabi2:accent_asc/narabi3:mola_asc/yure:visible/curve:fujisaki/details:invisible/limit:20/word:発表%20要領%20～する%20学習%20新しい%20使う%20日
https://translate.google.com/#ja/zh-CN/
http://tangorin.com/examples/%E4%BD%BF%E3%81%86
http://tangorin.com/general/%E4%BD%BF%E3%81%86