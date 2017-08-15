# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from logodownload import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

IMAGES_STORE = settings.IMAGES_STORE

class ImagtestPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['imagUrl']
        imagName = item['imagName']
        # print(image_url)
        # print(imagName)
        yield scrapy.Request(image_url,meta={'item':item,'imagName':imagName,'image_url':image_url})

    # def item_completed(self, results, item, info):
    #     #对获取的图片重命名
    #     imagepath = [x["path"] for ok,x in results if ok]
    #     print(item['imagName'])
    #     os.rename(IMAGES_STORE+'\\'+imagepath[0],IMAGES_STORE+item['imagName']  + ".jpg")
    #     return item
    def file_path(self,request,response=None,info=None):
        # image = [x["path"] for ok, x in results if ok]
        #
        # if image:
        #     image_paths = [x['path'] for ok, x in results if ok]
        #     if not image_paths:
        #         raise DropItem("Item contains no images")

        item = request.meta['item']  # 通过上面的meta传递过来item
        imagName = request.meta['imagName']
        image_url=request.meta['image_url']
        print(111)
        print(imagName)
        print(image_url)
            # 图片文件名，item['carname'][index]得到汽车名称，request.url.split('/')[-1].split('.')[-1]得到图片后缀jpg,png
        image_guid = imagName + '.jpg'
            # 图片下载目录 此处item['country']即需要前面item['country']=''.join()......,否则目录名会变成\u97e9\u56fd\u6c7d\u8f66\u6807\u5fd7\xxx.jpg
            #filename = u'full/{0}/{1}'.format(item['country'], image_guid)
        filename = u'full/{0}'.format(image_guid)

        return filename
