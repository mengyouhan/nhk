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

        sa = re.sub(r"(<rt>.{1,14}</rt>)", '', str(y))
        soup2 = BeautifulSoup(sa, 'lxml')
        su = [x.get_text() for x in soup2][0].strip()

        yuanwen = re.sub(r"\n", '', su)
        # print(type(la))
        return yuanwen


# new = GetNews()
# url1 = 'http://www3.nhk.or.jp/news/easy/k10010861721000/k10010861721000.html'
# url2 = 'http://www3.nhk.or.jp/news/easy/k10010876321000/k10010876321000.html'
#
#
# print(new.start(url1))
# print("_________________")
# print(new.start(url2))
