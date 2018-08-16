# -*- coding: utf-8 -*-
import csv

from bs4 import BeautifulSoup
import requests
import mycsv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 请求头设置
header = {
    'Accept': '*/*;',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'book.douban.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}


# 初始化csv文件
def info(name):
    csvinfo = open(name + '.mycsv', 'ab')
    begcsv = csv.writer(csvinfo)
    begcsv.writerow(['titles', 'authors', 'nums', 'peoples'])
    csvinfo.close()


# 爬取指定name模块的url,并存储至name.csv文件
def web(url, name):
    db_data = requests.get(url, headers=header)
    soup = BeautifulSoup(db_data.text, 'lxml')
    titles = soup.select('#subject_list > ul > li > div.info > h2 > a')
    authors = soup.select('#subject_list > ul > li > div.info > div.pub')
    nums = soup.select('#subject_list > ul > li > div.info > div.star.clearfix > span.rating_nums')
    peoples = soup.select('#subject_list > ul > li > div.info > div.star.clearfix > span.pl')
    print(titles[0])
    for title, author, num, people in zip(titles, authors, nums, peoples):
        data = [
            (
                title.get('title'),
                author.get_text().replace(' ', '').replace("\n", ""),
                num.get_text().replace(' ', '').replace("\n", ""),
                people.get_text().replace(' ', '').replace("\n", "")
            )
        ]
        csvfile = open(name + '.mycsv', 'ab')
        writer = csv.writer(csvfile)
        print(data)
        writer.writerows(data)
        csvfile.close()

def setCsv(name):
    url = 'https://book.douban.com/tag/' + name
    urls = [('https://book.douban.com/tag/' + name + '?start={}&type=T').format(str(i)) for i in range(20, 980, 20)]
    info(name=name)
    web(url, name)
    for single_url in urls:
        print(single_url)
        web(single_url, name=name)


if __name__ == '__main__':

    setCsv('管理')

    # 经管
    '''
    经管 ————经济学
                url = 'https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6'
                urls = ['https://book.douban.com/tag/%E7%BB%8F%E6%B5%8E%E5%AD%A6?start={}&type=T'.format(str(i)) for i in range(20,980,20)]
        ————管理
                url = 'https://book.douban.com/tag/%E7%AE%A1%E7%90%86'
                urls = ['https://book.douban.com/tag/%E7%AE%A1%E7%90%86?start={}&type=T'.format(str(i)) for i in range(20,980,20)]
        ————商业
                url = 'https://book.douban.com/tag/%E5%95%86%E4%B8%9A'
                urls = ['https://book.douban.com/tag/%E5%95%86%E4%B8%9A?start={}&type=T'.format(str(i)) for i in range(20,980,20)]
        ————金融
                url = 'https://book.douban.com/tag/%E9%87%91%E8%9E%8D'
                urls = ['https://book.douban.com/tag/%E9%87%91%E8%9E%8D?start={}&type=T'.format(str(i)) for i in range(20,980,20)]
        ————投资
                url = 'https://book.douban.com/tag/%E6%8A%95%E8%B5%84'
                urls = ['https://book.douban.com/tag/%E6%8A%95%E8%B5%84?start={}&type=T'.format(str(i)) for i in range(20,980,20)]
        ————营销
                url = 'https://book.douban.com/tag/%E8%90%A5%E9%94%80' 
                urls = ['https://book.douban.com/tag/%E8%90%A5%E9%94%80?start={}&type=T'.format(str(i)) for i in range(20,980,20)]
        ————创业
                url = 'https://book.douban.com/tag/%E5%88%9B%E4%B8%9A'
                urls = ['https://book.douban.com/tag/%E5%88%9B%E4%B8%9A?start={}&type=T'.format(str(i)) for i in range(20,980,20)]
        ————理财
                url = 'https://book.douban.com/tag/%E7%90%86%E8%B4%A2'
                urls = ['https://book.douban.com/tag/%E7%90%86%E8%B4%A2?start={}&type=T'.format(str(i)) for i in range(20,980,20)]        
        ————广告
                url = 'https://book.douban.com/tag/%E5%B9%BF%E5%91%8A'
                urls = ['https://book.douban.com/tag/%E5%B9%BF%E5%91%8A?start={}&type=T'.format(str(i)) for i in range(20,980,20)]        
        ————股票
                url = 'https://book.douban.com/tag/%E8%82%A1%E7%A5%A8'
                urls = ['https://book.douban.com/tag/%E8%82%A1%E7%A5%A8?start={}&type=T'.format(str(i)) for i in range(20,980,20)]        
        ————企业史
                url = 'https://book.douban.com/tag/%E4%BC%81%E4%B8%9A%E5%8F%B2'
                urls = ['https://book.douban.com/tag/%E4%BC%81%E4%B8%9A%E5%8F%B2?start={}&type=T'.format(str(i)) for i in range(20,980,20)]        
        ————策划 
                url = 'https://book.douban.com/tag/%E7%AD%96%E5%88%92'
                urls = ['https://book.douban.com/tag/%E7%AD%96%E5%88%92?start={}&type=T'.format(str(i)) for i in range(20,980,20)]        
    '''
    # 文学
    '''
    小说(5109791)	外国文学(1848096)	文学(1497245)	随笔(1091642)
    中国文学(991604)	经典(879878)	日本文学(783118)	散文(662803)
    村上春树(426750)	诗歌(313948)	童话(283996)	儿童文学(226203)
    古典文学(221902)	王小波(216675)	杂文(211192)	名著(210264)
    余华(195649)	张爱玲(186736)	当代文学(138446)	钱钟书(101534)
    外国名著(90667)	鲁迅(86468)	诗词(76603)	茨威格(60985)
    米兰·昆德拉(52181)	杜拉斯(43605)	港台(7301)
    '''
    # wenhua
    '''
    历史(1975187)	心理学(1294235)	哲学(1079313)	传记(748753)
    wenhua(687620)	社会学(651737)	艺术(476747)	设计(390797)
    社会(373323)	政治(347987)	建筑(263988)	宗教(243615)
    电影(236155)	政治学(213637)	数学(212776)	回忆录(166462)
    中国历史(164788)	思想(150224)	国学(139530)	人文(119389)
    人物传记(117486)	音乐(117374)	艺术史(110286)	绘画(107962)
    戏剧(103130)	二战(69508)	军事(69468)	西方哲学(69426)
    佛教(69257)	近代史(63349)	考古(48747)	自由主义(43490)
    美术(36425)
    '''
    # 生活
    '''
    爱情(845092)	旅行(555792)	生活(501905)	成长(491182)
    励志(381875)	心理(377500)	女性(293593)	摄影(285899)
    职场(204100)	教育(198911)	美食(188280)	游记(148636)
    灵修(121671)	健康(78868)	情感(78154)	两性(41344)
    手工(40233)	人际关系(39606)	养生(35557)	家居(22301)
    自助游(2668)
    '''
    # 科技
    '''
    科普(549874)	互联网(230343)	编程(152548)	科学(126786)
    交互设计(66973)	用户体验(53622)	算法(50159)	科技(24655)
    web(21660)	UE(5054)	交互(4800)	通信(4757)
    UCD(3553)	神经网络(2360)	程序(1266)
    '''
    # 流行
    '''
    漫画(1246111)	推理(901032)	绘本(872880)	青春(639962)
    东野圭吾(537782)	科幻(506381)	言情(491169)	悬疑(468237)
    奇幻(312917)	武侠(307337)	日本漫画(279805)	韩寒(262716)
    耽美(248630)	推理小说(245343)	亦舒(234634)	网络小说(204723)
    三毛(203603)	安妮宝贝(172977)	郭敬明(153286)	穿越(151218)
    阿加莎·克里斯蒂(149283)	金庸(148205)	轻小说(141159)	科幻小说(135473)
    青春文学(116265)	几米(114821)	魔幻(113367)	幾米(98274)
    张小娴(97656)	J.K.罗琳(84359)	古龙(74480)	高木直子(72256)
    沧月(65442)	校园(59711)	落落(58543)	张悦然(57753)
    '''
