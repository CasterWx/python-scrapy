import scrapy
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = "spider"

    def start_requests(self):
        urls = [
            'https://blog.csdn.net/bennyshi1998/article/details/79090136/',
            'https://blog.csdn.net/bennyshi1998/article/details/79402289/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body) 
        self.log('Saved file %s' % filename )
