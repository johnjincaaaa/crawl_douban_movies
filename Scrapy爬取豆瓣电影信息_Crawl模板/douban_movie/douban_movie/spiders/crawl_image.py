import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# 导入items里面的类
from ..items import DoubanMovieItem

class CrawlImageSpider(CrawlSpider):
    name = "crawl_image"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    rules = (
        # 规则一用于进入详情页
        Rule(LinkExtractor(restrict_xpaths='//div[@class="hd"]/a'), callback="parse_item", follow=False),
        # 规则二用于翻页
        Rule(LinkExtractor(restrict_xpaths='//span[@class="next"]/a'), follow=True),
    )

    def parse_item(self, response):    # response是详情页的响应对象

        image_url = response.xpath('//a[@class="nbgnbg"]/img/@src').get()
        image_name = response.xpath('//h1/span[1]/text()').get()
        print(image_url,image_name)
        # 实例化一个items类字典
        item = DoubanMovieItem()
        # 添加图片链接进入字典自动以加密的哈希值作为名字保存图片
        item['image_urls'] = [image_url]
        item['image_name'] = image_name

        return item
