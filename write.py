from fc import Word

class WriteMd():
    # def __init__(self):
    #     self.
    def start(self,url,yuanwen):
        yuanwen_fc = yuanwen.split('。')

        f = open('/Users/user/Desktop/zzz.md', 'w', encoding='utf8')

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
            str10 = '''

>{juzi}

            '''.format(juzi=j)
            f.write(str10 + '\n')

            find_word = Word(j).start()
            # find_word = ['抱える: 【 かかえる 】', 'まくる: 【 まくる 】', 'トラウマ: 【 とらうま 】', '夏: 【 なつ 】', '暑い: 【 あつい 】', 'さ: 【 さ 】',
            #              'せい: 【 せい 】', '形: 【 かたち / かた / なり 】']
            find_word_d = [x.split(':')[0] for x in find_word]
            for i, y in zip(find_word_d, find_word):
                # 分词
                hj = 'http://dict.hjenglish.com/jp/jc/{}'.format(i)
                goo = 'http://dictionary.goo.ne.jp/srch/all/{}/m0u/'.format(i)
                chaxun = 'gethj()'
                str11 = '''
-------
{y}  [沪江小D]({hj})  [goo辞书]({goo})<br>
``ffsdfafd``

                '''.format(y=y, hj=hj, goo=goo)
                f.write(str11 + '\n')
                # 翻译 调用google

        str3 = '''

-------
附没有假名的原文（方便查单词）：
>{yuanwen}
        '''.format(yuanwen=yuanwen)

        f.write(str3 + '\n')
        f.close()

