

BOT_NAME = "douban_movie"

SPIDER_MODULES = ["douban_movie.spiders"]
NEWSPIDER_MODULE = "douban_movie.spiders"

ADDONS = {}


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 最大并行数16，默认为3
CONCURRENT_REQUESTS = 3

# 等待时间1秒,太快会封IP
DOWNLOAD_DELAY = 1

# 个人爬取偏好
ITEM_PIPELINES = {

   # 这是pipelines文字数据保存在mongodb的管道
   # "douban_movie.pipelines.DoubanMoviePipeline": 300,
   # 这是pipeline图片数据的管道
   # "douban_movie.pipelines.DoubanImagePipeline" : 301,
   # 这是pipelines文字数据保存在csv文件里的管道
   # "douban_movie.pipelines.DoubanMovieCsvPipeline" :302
}

# 图片保存的位置，默认当前路径
IMAGES_STORE = './'


FEED_EXPORT_ENCODING = "utf-8"
