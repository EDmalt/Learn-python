# By hefei
# @File : crawler02.py
import requests
import time
from fake_useragent import UserAgent
from lxml import html

# 爬虫原理
"""
1.获取网页源文件
2.解析源文件
3.获取数据
"""


def get_html(url):
    # 使用动态headers伪装来破解反爬虫机制
    user_agent = UserAgent()
    headers = {"user-agent": user_agent.random}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception("请检查你的URL地址", url)  # 抛出异常
    return response.text


if __name__ == '__main__':
    url = "https://movie.douban.com/top250?start={}"
    html_str = get_html(url)  # 获取网页源文件
    etree = html.etree  # 获取一个解析对象
    num=0
    for i in range(10):
        html_str = get_html(url.format(i*25))  # 获取网页源文件--翻页方法
        html = etree.HTML(html_str)
        movies_xpath = html.xpath('//*[@id="content"]/div/div[1]/ol/li')  # 需要爬取对象的xpath

        for xp in movies_xpath:
            num+=1
            spans = xp.xpath('./div/div[2]/div[1]/a/span')
            movies_title = ""
            for span in spans:
                movies_title += span.text
            movies_info = xp.xpath('./div/div[2]/div[2]/p[1]')[0].text
            movies_score = xp.xpath('./div/div[2]/div[2]/div')[0].text
            print(num,":",movies_title,"\n\t", movies_info,"\n\t", movies_score)
        time.sleep(5)
