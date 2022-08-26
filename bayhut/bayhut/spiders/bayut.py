from email.policy import default
from gc import callbacks
import scrapy
#create class for store the values. 
class BayutSpider(scrapy.Spider):
    name ='bayut'
#start_urls is used for crawl the web site.
    start_urls =['https://www.bayut.com/to-rent/property/dubai/']
# the custom_setting is implemented for stop the close the spider.
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 100}
# define the function parse for store the data form the website. 
    def parse(self, response,):
        for products in response.css('article.ca2f5674'):
            yield{
                'location':products.css('div._7afabd84::text').get(),
                'price':products.css('span.f343d9ce::text').get(),
                'type':products.css('div._9a4e3964::text').get() ,
                'link':products.css('a._287661cb').attrib['href'] , 
            }
# the next_page is used to going to another page link.
        for next_page in response.css('a.b7880daf'):
            yield response.follow(next_page, self.parse)
    
    
          
             
    
    
        
            
    
            
    
        

