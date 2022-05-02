# By hefei
"""
@File : python_os.py
"""
# os模块
import os

file_path = "python_io.py"
# 判断文件是否存在
if not os.path.exists(file_path):
    print("文件不存在")
else:
    with open(file_path, "r", encoding="utf-8") as file:

        # print(file.read(100))
        # print(file.readlines())  # readlines()返回类型是列表
        """
         for line in file.readlines():
            print(line,end="")
        print("-"*20)
        """
        # 使用readline()读取文件
        line = file.readline()
        while line:
            print(line, end="")
            line = file.readline()

print(os.name)  # 查询操作系统名称
print(os.getenv("path"))  # 查询环境变量配置
print(os.getcwd())  # 获取当前工作目录
print(os.listdir())  # 获取当前目录下所有文件和文件夹

# os.path.isfile()判断是否是文件
# full_path = file_path+"\\"+file # 低级拼接路径方法
# full_path=os.path.join(file_path,file) # 常用拼接路径方法
