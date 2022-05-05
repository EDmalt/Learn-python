# By hefei
# @File : crawler.py
# 爬虫原理
"""
1.获取网页源文件
2.解析源文件
3.获取数据
"""
# 导入包
import requests # 获取源文件类
from fake_useragent import UserAgent
from lxml import html # 解析源文件类

# url = "https://movie.douban.com/top250"  # 获取地址
url_XinLang = "https://www.sina.com.cn/"

# 反爬虫机制--主要是根据请求头文件的方式来反爬虫
# headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
# "Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}

# 使用动态headers伪装来破解反爬虫机制
user_agent = UserAgent()
headers = {"user-agent": user_agent.random}

# respone = requests.get(url, headers=headers)
rsp = requests.get(url_XinLang)
# 重新转码
html_str = rsp.text
html_str = str(html_str.encode("ISO-8859-1"), encoding="UTF-8")

print(rsp.status_code)  # 查询网站状态
# print(rsp.text)

# 解析
etree = html.etree  # 获取解析对象
html_obj = etree.HTML(html_str)

# 只获取新闻标题
url_news_top_a = html_obj.xpath('//*[@id="syncad_0"]/ul[1]/li[2]/a[1]')
for a in url_news_top_a:
    print(a.text)
# 获取超链接
url_news_top_a_href=html_obj.xpath('//*[@id="syncad_0"]/ul[1]/li[2]/a[1]/@href')
for href in url_news_top_a_href:
    print(href)

# 同时爬取标题和超链接
url_news_top_a=html_obj.xpath('//*[@id="syncad_0"]/ul/li/a')
for a in url_news_top_a:
    print(a.xpath("./text()")[0],a.xpath("./@href")[0])
