# coding=utf-8
import sys
import csv
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
# 请求头设置

def download(url):
    db_data = requests.get(url)
    soup = BeautifulSoup(db_data.text, 'lxml')
    titles = soup.select(
        'body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.des > h2 > a:nth-of-type(1)')
    houses = soup.select('body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.des > p.room')
    oneaddresss = soup.select(
        'body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.des > p.add > a:nth-of-type(1)')
    twoaddresss = soup.select(
        'body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.des > p.add > a:nth-of-type(2)')
    prices = soup.select(
        'body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.listliright > div.money > b')
    for title, house, oneaddress, twoaddress, price in zip(titles, houses, oneaddresss, twoaddresss, prices):
        data = [
            (
                str(title.string).replace(' ', '').replace('\n', ''),
                house.get_text().split(' ')[0].replace(' ', '').replace("\n", ""),
                house.get_text().split(' ')[-1].replace(' ', '').replace("\n", ""),
                oneaddress.get_text().replace(' ', '').replace("\n", ""),
                twoaddress.get_text().replace(' ', '').replace("\n", ""),
                price.get_text().replace(' ', '').replace("\n", "")
            )
        ]

        csvfile = open('kf.csv', 'ab')
        writer = csv.writer(csvfile)
        print('get :' + url)
        writer.writerows(data)
        csvfile.close()


# 初始化csv文件
def info():
    csvinfo = open('kf.csv', 'ab')
    begcsv = csv.writer(csvinfo)
    begcsv.writerow(['title', 'house', 'area', 'address1', 'address2', 'price'])
    csvinfo.close()


if __name__ == '__main__':
    # info()
    url = 'http://kaifeng.58.com/chuzu/pn38/?PGTID=0d3090a7-0092-6bc0-64cf-c11bc3695d2f&ClickID=2'
    download(url)
