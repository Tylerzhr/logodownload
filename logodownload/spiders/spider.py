import scrapy
import string
from logodownload.items import ImagtestItem
from scrapy import Request

class scapyimage(scrapy.Spider):
    name = "imag"
    def start_requests(self):
        #不存在的车系开头
        for x in string.ascii_uppercase:
            if x not in "EIUV":
                url = "http://www.autohome.com.cn/grade/carhtml/" + x + ".html"
                yield Request(url,self.get_brand)

    def get_brand(self,response):
        item=ImagtestItem()
        dls = response.xpath("//dl")
        for dl in dls:
            car_brand_imagUrl = format(dl.xpath("./dt/a/img/@src").extract()).replace("['", '').replace("']", '')
            car_brand_name = format(dl.xpath("./dt/div/a/text()").extract()).replace("['", '').replace("']", '')
            item['imagUrl']=car_brand_imagUrl
            item['imagName']=car_brand_name
            #print(item['imagUrl'])
            #print(item['imagName'])
            yield item