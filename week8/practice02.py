# By hefei
"""
@File : practice02.py
"""

# 统计windows下所有文件和文件夹的数目
import os

file_path = r"C:\Windows"
file_num = 0 # 统计文件数目
folder_num = 0 # 统计文件夹数目
for file in os.listdir(file_path):
    # full_path = file_path+"\\"+file # 低级拼接路径方法
    full_path=os.path.join(file_path,file) # 常用路径拼接方式
    if os.path.isfile(full_path):
        file_num += 1
    else:
        folder_num += 1

print("windows目录下总共{}，有{}文件和{}文件夹".format(len(os.listdir(file_path)), file_num, folder_num))
