# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class DoubanMoviePipeline:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['豆瓣']
        self.collection = self.db['scrapy_movie_crawl']

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item

    def __del__(self):
        self.client.close()

class DoubanImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        data = {'data':item}
        return [Request(u,meta=data) for u in urls]

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta.get('data')
        image_name :str= item.get('image_name')
        image_name = image_name.replace(':','：').replace('.','。')
        return f"image/{image_name}.jpg"