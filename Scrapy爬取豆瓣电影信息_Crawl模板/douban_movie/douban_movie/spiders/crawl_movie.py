import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlMovieSpider(CrawlSpider):
    name = "crawl_movie"
    allowed_domains = ["movie.douban.com"]
    # 第一次请求
    start_urls = ["https://movie.douban.com/top250"]

    # 规则元组
    rules = (
        # LinkExtractor用于筛选链接（正则或者xpath筛选(xpath只需定位到标签位置，无需去属性)）（第二次请求）, follow指是否跟随详情页匹配的链接的跳转

        # 规则一用于进入详情页
        Rule(LinkExtractor(restrict_xpaths='//div[@class="hd"]/a'), callback="parse_item", follow=False),
        # 规则二用于翻页
        Rule(LinkExtractor(restrict_xpaths='//span[@class="next"]/a'), follow=True),
    )
    # 第二次请求返回的response
    def parse_item(self, response):
        score= response.xpath('//strong/text()').get()
        name = response.xpath('//h1/span[1]/text()').get()
        movie_url = response.url
        description = response.xpath('//span[@property="v:summary"]/text()').get()
        description = ''.join(description).replace(' ', '').replace('\u3000', '').replace('\n', '')
        item = {'name':name,'movie_url':movie_url,'score':score,'description':description}#是一个字典
        # 返回给管道保存
        return item
