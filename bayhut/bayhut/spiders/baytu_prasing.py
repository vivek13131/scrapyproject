from email.policy import default
from gc import callbacks
import scrapy
class scrapy(scrapy.Spider):
    name ='prasing'
    start_urls =['https://www.bayut.com/property/details-5118159.html']
    
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
                "size":response.xpath("//span[@class='fc2d1086']//span/text()").extract(),
                 
                
            },
            "permit_number":response.xpath("//span[@class='ff863316']/text()")[4].extract(),
            "agent_name":response.xpath("//span[@class='ff863316']/text()")[0].extract(),
            "image_url":response.xpath("//img[@class='bea951ad']/@src").get(),
            "brudcrumb":response.xpath("//span[@class='_327a3afc']/text()").extract(),
            "amenities":[
                response.xpath("//span[@class='_005a682a']/text()").extract(),
            ],
            "description": response.xpath("//span[@class='_2a806e1e']/text()").extract(),          
          }
          
             
    
    
        
            
    
            
    
        


    