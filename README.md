# Python Web Crawler Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 项目概述

本项目是一个基于Python的网络爬虫工具，用于从豆瓣电影网站抓取电影信息并进行简单的数据处理和分析。它提供了以下功能：

- 爬取豆瓣电影Top250的电影信息（名称、评分、导演、主演等）
- 支持数据导出到mongodb数据库
- 支持数据导出到本地csv文件里
- 支持电影图片爬取到本地
- 可配置的爬取参数（如爬取间隔、超时设置）

## 安装指南

### 环境要求
- scrapy 3.12.0或更早的版本
- Python 3.8或更高版本
- pip包管理器


### 安装步骤

1. 克隆项目仓库(或者直接下载)：
   ```bash
   git clone https://github.com/yourusername/douban-movie-crawler.git

2. 安装依赖包：
   ```bash
   pip install -r requirements.txt

# 好了，现在进入个人爬取偏好环节 


## 爬取设置 setting.py
CRAWL_DELAY = 2  # 爬取间隔(秒)，避免过快请求被封IP
MAX_RETRIES = 3  # 请求失败时的最大重试次数
TIMEOUT = 10  # 请求超时时间(秒)

# 数据保存设置
OUTPUT_FORMAT = 'csv'  # 输出格式：csv或json
OUTPUT_FILE = 'douban_top250.csv'  # 输出文件名
运行爬虫
执行以下命令启动爬虫：

bash
python main.py

爬取完成后，数据将保存在指定的输出文件中。
数据分析
爬取完成后，你可以使用以下命令进行简单的数据分析：

bash
python analyze.py

这将生成一些基本的统计信息和可视化图表。
代码结构
项目的主要文件和目录结构如下：

plaintext
douban-movie-crawler/
├── main.py               # 主程序入口
├── crawler.py            # 爬虫核心模块
├── parser.py             # 页面解析模块
├── data_handler.py       # 数据处理模块
├── config.py             # 配置文件
├── analyze.py            # 数据分析模块
├── requirements.txt      # 依赖包列表
├── .gitignore            # Git忽略文件
└── README.md             # 项目说明文档
示例代码
以下是爬虫核心模块的部分代码示例：

python
运行
# crawler.py

import requests
from bs4 import BeautifulSoup
import time
import random
import logging
from config import *

class DoubanCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.logger = logging.getLogger('douban_crawler')
        
    def fetch_page(self, url):
        """发送HTTP请求获取页面内容"""
        retries = 0
        while retries < MAX_RETRIES:
            try:
                time.sleep(CRAWL_DELAY + random.uniform(0, 1))  # 随机延时，避免请求过于频繁
                response = requests.get(url, headers=self.headers, timeout=TIMEOUT)
                response.raise_for_status()  # 检查请求是否成功
                return response.text
            except requests.RequestException as e:
                self.logger.error(f"请求失败: {url}, 错误: {e}")
                retries += 1
                self.logger.info(f"正在重试 ({retries}/{MAX_RETRIES})...")
        self.logger.error(f"请求 {url} 超过最大重试次数")
        return None
        
    def parse_movie_info(self, html):
        """解析电影信息"""
        soup = BeautifulSoup(html, 'html.parser')
        movie_list = []
        
        for item in soup.select('div.item'):
            try:
                title = item.select_one('span.title').text.strip()
                rating = item.select_one('span.rating_num').text.strip()
                director = item.select_one('div.bd p').text.strip().split('\n')[0].replace('导演: ', '')
                quote = item.select_one('span.inq')
                quote = quote.text.strip() if quote else '暂无简介'
                
                movie = {
                    'title': title,
                    'rating': float(rating),
                    'director': director,
                    'quote': quote
                }
                movie_list.append(movie)
            except Exception as e:
                self.logger.error(f"解析错误: {e}")
                
        return movie_list
        
    def crawl_top250(self):
        """爬取豆瓣电影Top250"""
        all_movies = []
        
        for start in range(0, 250, 25):
            url = f'https://movie.douban.com/top250?start={start}'
            self.logger.info(f"正在爬取: {url}")
            
            html = self.fetch_page(url)
            if not html:
                continue
                
            movies = self.parse_movie_info(html)
            all_movies.extend(movies)
            self.logger.info(f"已爬取 {len(movies)} 部电影，累计: {len(all_movies)} 部")
            
        return all_movies
贡献指南
我们欢迎任何人对本项目做出贡献。如果你有改进建议或发现了 bug，请遵循以下步骤：

Fork 本仓库
创建你的特性分支 (git checkout -b feature/your-feature)
提交你的更改 (git commit -am 'Add some feature')
将分支推送到远程仓库 (git push origin feature/your-feature)
创建 Pull Request
许可证
本项目采用 MIT 许可证。有关详细信息，请参阅LICENSE文件。
联系信息
如果你有任何问题或建议，请通过以下方式联系我们：

邮箱：your.email@example.com
GitHub Issues：https://github.com/yourusername/douban-movie-crawler/issues

plaintext

你可以根据实际项目情况调整内容，特别是项目名称、功能描述、代码示例和联系方式等部分。如果需要更详细的说明或有其他特殊
