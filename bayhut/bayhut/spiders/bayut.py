from email.policy import default
from gc import callbacks
import scrapy
class BayutSpider(scrapy.Spider):
    name ='bayut'
    start_urls =['https://www.bayut.com/to-rent/property/dubai/']
    base_url =['https://www.bayut.com/to-rent/property/dubai/']
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 20}
    
    def parse(self, response,):
        for products in response.css('article.ca2f5674'):
            yield{
                'location':products.css('div._7afabd84::text').get(),
                # 'price':products.css('span.f343d9ce::text')[1500].get(),
                # 'type':products.css('div._9a4e3964::text')[1500].get() ,
                # 'link':products.css('a._287661cb')[1500].attrib['href'] ,
                
            }
   
        for next_page in response.css('a.b7880daf'):
            yield response.follow(next_page, self.parse)
    
    # def parse(self, response,):
    #       yield{
              
    #           'productit':response.xpath("//span[@class='_327a3afc']/text()")[4].extract(),
                
    #       }
          
             
    
    
        
            
    
            
    
        

