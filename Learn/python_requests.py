# By hefei
"""
@File : python_requests.py
"""
import requests  # 导入requests库

# 可以通过字符串字典来向url地址传递参数
data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
r_get = requests.get("https://www.sonkwo.cn/")  # 向目标地址发送get请求，，然后获取一个response 使用params来传递参数
r_post = requests.post("https://www.bilibili.com/")  # 向目标地址发送post请求，，然后获取一个response
r_put = requests.put("https://www.bilibili.com/")
print(r_get.text)  # 输出获取的内容
print(r_get.url)
