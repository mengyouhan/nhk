from bs4 import BeautifulSoup
import requests
import os,re,time
from selenium import webdriver


class Word(object):
    def __init__(self, text):
        self.text = text
    def start(self):
        # PhantomJS
        driver = webdriver.PhantomJS()
        url = 'http://language.tiu.ac.jp/'

        driver.get(url)

        time.sleep(3)
        aa = driver.page_source
        driver.find_element_by_css_selector(
            "body > center > form > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(2) > td > textarea").send_keys(
            self.text)
        time.sleep(3)

        driver.find_element_by_css_selector(
            "body > center > form > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td > input:nth-child(1)").click()

        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(12)
        driver.switch_to.frame("dic")
        soup = BeautifulSoup(driver.page_source, 'lxml')

        time.sleep(12)
        select1 = "#overflowbox  font[size=3]"
        # soup.select(select1)

        a1 = [x.get_text() for x in soup.select(select1)]

        select2 = "#overflowbox > font[size=2]"
        # print(soup.select(select2))

        # a2 = [x.get_text() for x in soup.select(select2)]

        a2 = []
        # soup.find_all(size="3").next_sibling
        for x in soup.find_all(size="3"):
            a2.append(x.next_sibling.get_text())

        li = []
        for aa1, aa2 in zip(a1, a2):
            # print(aa1 + ': ' + aa2)
            li.append(aa1 + ': ' + aa2)
        print(li)
        # z = ''
        #
        # for y in li:
        #     # ww = y
        #     word = y.split(':')[0]
        #     word1 = y.split(':')[0]
        #
        #     hujiang = 'http://dict.hjenglish.com/jp/jc/{}'.format(word)
        #     goo = 'http://dictionary.goo.ne.jp/srch/all/{}/m0u/'.format(word)
        #     last = '''
        #             <h3>{y}</h3>
        #             <span><a href='{hujiang}'>hujiang</a></span>
        #             <span><a href='{goo}'>goo</a></span>
        #
        #             '''.format(y=y, hujiang=hujiang, goo=goo)
        #     z += last

        return li
# x = Word('抱えまくったトラウマが 夏の暑さのせいで 形を…')
# x.start()
# print(x.start())





