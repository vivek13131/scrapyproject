import scrapy
class BayutSpider(scrapy.Spider):
    name ='bayut'
    start_urls =['https://www.bayut.com/to-rent/property/dubai/']
    
    def parse(self, response,):
        for products in response.css('article.ca2f5674'):
            yield{
                'location':products.css('div._7afabd84::text').get(),
                'price':products.css('span.f343d9ce::text').get(),
                'type':products.css('div._9a4e3964::text').get() ,
                'link':products.css('a._287661cb').attrib['href'] ,
                
            }
        

