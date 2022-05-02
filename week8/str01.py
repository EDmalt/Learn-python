# By hefei
# str类字符串不可变
"""
创建字符串的几种方式
str1=str()
str2="xxx"
"""
# 基于python的缓存机制，如果定义的变量值已经存在，则不会开启新的内存空间
str1 = str()
str2 = ""
print(id(str1), "\t", id(str2))
print(str1 == str2)  # 比较值
print(str1 is str2)  # 比较内存地址空间

# 字符串基本操作
str_a = "abcde"
print(str_a.isalnum())  # 判断字符串是否由数和字母组成
print(str_a.isalpha())  # 判断字符串是否由全字母组成

str_num = "123123"
str_u = "\u00b2"
print(str_num.isnumeric())  # 判断是否为纯数字 全半角都支持
print(str_num.isdecimal())  # 判断是是否为纯数字，一般指英文输入法下
print(str_u.isdigit())  # 判断是否为纯数字，且支持Unicode编码

str_true = "2^&%*"
print(str_true.isidentifier())  # 判断其是否为合法标识符

str_url = "http://www.google.com"
print(str_url.startswith("www"))  # 判断字符串是否以这个为开头
print(str_url.endswith("com"))  # 判断字符串的结尾是不是这个
print(str_url.rfind("."))  # 查找字符再字符串中的位置
print(str_url.count("."))  # 查找该字符出现的次数
print(str_url.capitalize())  # 首字母大写
print("字母全小写", str_url.lower(), "\n字母全大写", str_url.upper())  # 字母大小写转换
print("标题格式 即每个单词首字母大写", str_url.title())
print("替换", str_url.replace("google", "steam"))  # 替换字符串中的字符
