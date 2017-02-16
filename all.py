from easy import GetNews
from fc import Word
from write import WriteMd


new = GetNews()

url2 = 'http://www3.nhk.or.jp/news/easy/k10010876321000/k10010876321000.html'

yuanwen = new.start(url2)

WriteMd().start(url2,yuanwen)