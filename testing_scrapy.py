# -*- coding: utf-8 -*-
"""
Spyder Editor
Scrapping miniproject
how handle to
scrapy crawl name
"""

from scrapy import spiders as sc
from scrapy import Spider
from scrapy import Selector
from scrapy.item import Item,Field # caprura dado nao estruturados scraping em dados estrturados
from scrapy.http import Response
from scrapy.loader import ItemLoader # popular items scrapded em container parsear dados crus antes de classi

url = 'http://'
class ExtractorSamples(Spider):
    name = "testing"
    
    @classmethod
    def start_request(self):
        return sc.Request(url,callback=self.parser,method='GET')

    def parser(self):
        response = Response.url('')
        tag = response.xpath('div:text').get()
        if reponse.status == 200:
            yield {'from': response.header, 'content' : response.text}
        else: raise SpiderError
    
    def parser(self,response):
        load = ItemLoader(item = Item(x),response=response)
        load.add_xpath()
        load.add_value()
        return load.load_item()
    
class Items(Item):
    x = Field()