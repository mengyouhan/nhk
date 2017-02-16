from bs4 import BeautifulSoup
import requests
import os,re,time
from selenium import webdriver

# PhantomJS
class GetNewsLists():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def start(self,url):
        self.driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        #获取新闻日期
        select = "#monthly .weeklist .heightLineParent a"
        y1 = soup.select(select)
        newDate = [x['id'] for x in y1]
        dict = {}

        #点击选择新闻日期
        # select_date = '#'+newDate[2]
        self.driver.find_element_by_css_selector("#monthly > div > ul > li:nth-child(2)").click()
        time.sleep(5)
        #获取新闻列表
        soup2 = BeautifulSoup(self.driver.page_source, 'lxml')
        select2 = "ul.newslisteven a"
        y2 = soup2.select(select2)

        dict[newDate[2]] = ['http://www3.nhk.or.jp/news/easy' + x['href'][1:] for x in y2]
        return dict
print(GetNewsLists().start('http://www3.nhk.or.jp/news/easy/index.html'))
#monthly > div > ul > li:nth-child(2)