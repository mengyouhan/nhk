from fc import Word
from bs4 import BeautifulSoup
import requests,os,time
# q = '固まる'

class WriteMd():
    # def __init__(self):
    #     self.




    def start(self,url,yuanwen):

        def gethj(w):
            try:
                # q = x.split(':')[0]
                url = 'http://dict.hjenglish.com/jp/jc/{}'.format(w)
                UA = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"
                headers = {'User-Agent': UA}
                wb_data = requests.get(url, headers=headers)
                time.sleep(5)
                soup = BeautifulSoup(wb_data.text, 'lxml')
                select = "#headword_jp_1 > div.simple_content.mt10"
                # soup.select(select)
                time.sleep(10)
                CC = [x.get_text() for x in soup.select(select)]
                # print(w)

                print('查询成功')
                return str(CC[0])
            except:
                print('查询失败')
                return ' '

        yuanwen_fc = yuanwen.split('。')

        f = open('/Users/user/Desktop/xxx.md', 'w', encoding='utf8')

        url_jia = url
        url_mp3 = url[:-4]+'mp3'
        str1 = '''
>[假名，音频版新闻地址]({url_jia}) <br>
>[假名，音频mp3地址]({url_mp3}) <br>

新闻详情：

        '''.format(url_jia=url_jia, url_mp3=url_mp3)

        f.write(str1 + '\n')

        # 句子原文
        for j in yuanwen_fc:
            find_word = Word().start(j)
            # find_word = ['抱える: 【 かかえる 】', 'まくる: 【 まくる 】', 'トラウマ: 【 とらうま 】', '夏: 【 なつ 】', '暑い: 【 あつい 】', 'さ: 【 さ 】',
            #              'せい: 【 せい 】', '形: 【 かたち / かた / なり 】']
            find_word_d = [x.split(':')[0] for x in find_word]
            # ojad = 'http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/sortprefix:accent/narabi1:kata_asc/narabi2:accent_asc/narabi3:mola_asc/yure:visible/curve:fujisaki/details:invisible/limit:20/word:'
            # for z in find_word_d:
            #     ojad = ojad+z+'%20'
            # 翻译调用google 语调发音ojad 分词jisho
            google = 'https://translate.google.com/#ja/zh-CN/{}'.format(j)
            str10 = '''

>{juzi}
[google翻译]({google}) [jisho分词](http://jisho.org/)

            '''.format(juzi=j,google = google)
            f.write(str10 + '\n')


            for i, y in zip(find_word_d, find_word):
                # 分词
                hj = 'http://dict.hjenglish.com/jp/jc/{}'.format(i)
                goo = 'http://dictionary.goo.ne.jp/srch/all/{}/m0u/'.format(i)
                tangorin = 'http://tangorin.com/general/{}'.format(i)
                jisho = 'http://jisho.org/search/{}'.format(i)
                ojad = 'http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/sortprefix:accent/narabi1:kata_asc/narabi2:accent_asc/narabi3:mola_asc/yure:visible/curve:fujisaki/details:invisible/limit:20/word:{}%20'.format(i)
                lizi = 'http://tangorin.com/examples/{}'.format(i)
                chaxun = gethj(i)

                str11 = '''
-------
{y}  [沪江小D]({hj}) [単語林]({tangorin}) [jisho]({jisho}) [goo辞书]({goo}) [语调发音]({ojad}) [例句]({lizi})<br>
``{chaxun}``

                '''.format(y=y, hj=hj,tangorin = tangorin,jisho =jisho,goo=goo,ojad=ojad,lizi = lizi,chaxun=chaxun)
                f.write(str11 + '\n')


        str3 = '''

-------
附没有假名的原文（方便查单词）：
>{yuanwen}
        '''.format(yuanwen=yuanwen)

        f.write(str3 + '\n')
        f.close()



