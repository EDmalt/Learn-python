# By hefei
# @File : Data_Crawling.py
"""
    该文件是用于爬取数据并保存为文件的模块
"""
import requests  # 导入requests库
from fake_useragent import UserAgent  # 导入fake_useragent中的UserAgent模块
from lxml import html  # 导入lxml库中的html模块
import pandas as pd  # 导入pandas库


def get_html(url):
    # 破解网站反爬虫机制
    user_agent = UserAgent()
    headers = {"user-agent": user_agent.random}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:  # 如果网页状态不为200则抛出异常
        raise Exception("请检查url地址", url)  # 抛出异常
    return response.text


if __name__ == '__main__':
    url = "https://www.cgmodel.com"  # 获取url地址
    name, price, label = [], [], []  # 创建三个列表保存爬取内容

    html_str = get_html(url)  # 获取网页源文件
    etree = html.etree  # 获取一个解析对象
    html = etree.HTML(html_str)
    data_xpath = html.xpath("/html/body/div[3]/div/div[1]/div[2]/div/div[2]/div[2]/ul/li")  # 爬取对象的xpath路径
    for xp in data_xpath:  # 将列表中的字符串拆分出来
        name += [xp.xpath("./p/a")[0].text]  # 通过拼接来爬取名称的相关内容
        price += [xp.xpath("./span")[0].text]
        """
            切换页面来获取标签
        """
        url = "https://www.cgmodel.com{}".format(xp.xpath("./p/a/@href")[0])  # 替换网页以便爬取标签
        html_str = get_html(url)  # 获取网页源文件--切换页面方法
        html = etree.HTML(html_str)

        label += [html.xpath('//*[@id="modeldeals"]/div[2]/div/a/text()')]

    """
        使用字典创建DataFrame并保存为csv文件
    """
    data = {
        "名称": name,
        "价格": price,
        "标签": label
    }
    pd.DataFrame(data).to_csv(r"E:\可删文件\Python\项目2\data.csv", encoding="UTF-8-sig")  # 设置保存路径并修改编码防止乱码
