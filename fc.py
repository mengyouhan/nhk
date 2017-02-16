from bs4 import BeautifulSoup
import requests
import os,re,time
from selenium import webdriver


class Word(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
    def start(self,text):
        # PhantomJS

        url = 'http://language.tiu.ac.jp/'

        self.driver.get(url)

        time.sleep(3)
        aa = self.driver.page_source
        self.driver.find_element_by_css_selector(
            "body > center > form > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td > textarea").send_keys(
            text)
        time.sleep(3)

        self.driver.find_element_by_css_selector(
            "body > center > form > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td > input:nth-child(1)").click()

        time.sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(12)
        self.driver.switch_to.frame("dic")
        soup = BeautifulSoup(self.driver.page_source, 'lxml')

        time.sleep(12)
        select1 = "#overflowbox  font[size=3]"


        a1 = [x.get_text() for x in soup.select(select1)]

        select2 = "#overflowbox > font[size=2]"


        a2 = []

        for x in soup.find_all(size="3"):
            a2.append(x.next_sibling.get_text())

        li = []
        for aa1, aa2 in zip(a1, a2):
            # print(aa1 + ': ' + aa2)
            li.append(aa1 + ': ' + aa2)
        print(li)
        time.sleep(12)

        return li






