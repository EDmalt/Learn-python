# By hefei
# @File : test.py

import requests
from fake_useragent import UserAgent
from lxml import html

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
    url = "http://221.10.100.185:8088/default2.aspx"
    html_str = get_html(url)  # 获取网页源文件
    etree=html.etree
    html=etree.HTML(html_str)
    value1=html.xpath('//*[@id="TextBox2"]/@value')
    print(value1)

