from gc import callbacks
import scrapy
class BayutSpider(scrapy.Spider):
    name ='bayut'
    start_urls =['https://www.bayut.com/to-rent/property/dubai/']
    base_url =['https://www.bayut.com/to-rent/property/dubai/']
    
    def parse(self, response,):
        for products in response.css('article.ca2f5674'):
            yield{
                'location':products.css('div._7afabd84::text').get(),
                'price':products.css('span.f343d9ce::text').get(),
                'type':products.css('div._9a4e3964::text').get() ,
                'link':products.css('a._287661cb').attrib['href'] ,
                
            }
        # next_page_partial_url = response.xpath('//li[@class="b7880daf"]/a/@href').extract_first()
        # next_page_url =self.base_url + next_page_partial_url
        # yield scrapy.Request(next_page_url, callback=self.parse)
        
        
        
        #  next_page =  response.css('a.b7880daf').attrib['href']
        # if next_page is not  None:
        #     yield response.follow(next_page, callback=self.parse)
        for next_page in response.css('a.b7880daf'):
            yield response.follow(next_page, self.parse)
        
    
    
        
            
    
            
    
        

