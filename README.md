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


## 爬取设置 `setting.py`(必选)
`DOWNLOAD_DELAY` =   # 爬取间隔(秒)，避免过快请求被封IP

`CONCURRENT_REQUESTS` = 3  # 请求失败时的最大并行数

`USER_AGENT` = ''  # 个人user_agent

`ITEM_PIPELINES` = # 需要哪种功能就取消注释，_一次只能取消一个注释_
   
  - ```-*若选300或302*：```
      -*先在`run_spider.py`取消注释# execute(['scrapy','crawl','crawl_movie'])，然后直接运行此文件
   
  - ```-*若选301*：```
      -*先在`run_spider.py`取消注释# execute(['scrapy','crawl','crawl_image'])，然后直接运行此文件


爬取完成后，数据将保存在指定的输出文件中。



贡献指南
我们欢迎任何人对本项目做出贡献。如果你有改进建议或发现了 bug，call me ~  >_< ：



邮箱：2912492958@qq.com

plaintext

