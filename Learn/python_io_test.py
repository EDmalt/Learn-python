# By hefei
"""
@File : python_io_test.py
"""
import os
import io

file_url = r"../week8/new.py"

with open(file_url, "w+") as file:
    file.write(input("请输入内容："))  # 向目标文件写入

