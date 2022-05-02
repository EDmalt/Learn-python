# By hefei
"""
@File : python_io.py
"""
# 内置函数open()：用于床创建一个对象并使用对象的read()和write()方法读写数据
# 变量名=open(文件路径,mode) mode是对象操作方式

# 操作 C:\Windows\System32\drivers\etc\networks 文件
# 路径创建方式(三种)
file_path = r"C:\Windows\System32\drivers\etc\networks"
file_path = "C:\\Windows\\System32\\drivers\\etc\\networks"
file_path = "C:/Windows/System32/drivers/etc/networks"

file = open(file_path, "r")  # 打开文件获取文件对象
print(file.read())
file.close()  # 记得关闭文件

# 高级操作
with open(file_path, "r") as file:  # 利用with关键字打开文件，自动关闭
    print(file.read())

