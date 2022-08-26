from email.policy import default
from gc import callbacks
import scrapy
class scrapy(scrapy.Spider):
    name ='prasing'
    start_urls =[
                 'https://www.bayut.com/property/details-5118159.html'
                 
                 ]
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 10}
    
    # def parse(self, response,):
    #     for products in response.css('article.ca2f5674'):
    #         yield{
    #             'location':products.css('div._7afabd84::text').get(),
    #             'price':products.css('span.f343d9ce::text').get(),
    #             'type':products.css('div._9a4e3964::text').get() ,
    #             'link':products.css('a._287661cb').attrib['href'] ,
                
    #         }
   
    #     for next_page in response.css('a.b7880daf'):
    #         yield response.follow(next_page, self.parse)
    
    def parse(self, response,):
          yield{
              "Productid":response.xpath("//span[@class='_327a3afc']/text()")[4].extract(),
            "purpose":response.xpath("//span[@class='_812aa185']/text()")[1].extract(),
            "type":response.xpath("//span[@class='_812aa185']/text()")[0].extract(),
            "addon":response.xpath("//span[@class='_812aa185']/text()")[3].extract(),
            "price":
                {
                "currency":response.xpath("//span[@class='e63a6bfb']/text()").extract(),
                "ammount":response.xpath("//span[@class='_105b8a67']/text()").extract(),
                },
            "location":response.xpath("//div[@class='_1f0f1758']/text()").extract(),
            "bed_bath_szie":
                {
                "bedrooms":response.xpath("//span[@class='fc2d1086']/text()")[0].extract(),
                "bathrooms":response.xpath("//span[@class='fc2d1086']/text()")[1].extract(),
                "size":response.xpath("//span[@class='fc2d1086']//span/text()").extract() 
                
            },
              
                
          }
          
             
    
    
        
            
    
            
    
        


    