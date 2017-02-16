# from easy import GetNews
# from fc import Word
from write import WriteMd


# new = GetNews()

url2 = 'http://www3.nhk.or.jp/news/easy/k10010876321000/k10010876321000.html'

# yuanwen = new.start(url2)
yuanwen = '文部科学省は、小学校と中学校で何をどのように教えるかなどを決めた「学習指導要領」を、１０年に１回ぐらい新しくしています。１４日、小学校では２０２０年、中学校では２０２１年から使う新しい学習指導要領の案を発表しました。'

WriteMd().start(url2,yuanwen)