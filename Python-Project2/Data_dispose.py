# By hefei
# @File : Data_dispose.py
"""
    这个文件主要用于数据处理并绘制图像
"""
import pandas as pd  # 导入pandas库
import numpy as np
import matplotlib.pyplot as plt  # 导入matplotlib库中的pyplot模块

data = pd.read_csv(r"E:\可删文件\Python\项目2\data.csv")  # 将其导入为全局变量


def plt_init():
    # 修改配置以显示中文
    plt.figure()  # 生成画布
    plt.rcParams['font.sans-serif'] = ["SimHei"]
    plt.title("某模型网站实时销售价格", fontsize=16)
    plt.xlabel("标签", fontsize=15)  # 设置图标xy轴标签("显示文字",fontsize设置线条大小)
    plt.ylabel("价格(RMB)", fontsize=15)


if __name__ == '__main__':
    """
     数据整理部分
    """
    data.loc[:, "简称"] = data["标签"].str.split("'").str[1]  # 获取第一个标签用于标识
    data.loc[:, "价格"] = data["价格"].str.replace("￥", "").astype("float64")  # 将价格换为浮点型
    money = np.array(data["价格"])  # 将价格转换为np数组
    """
        新增一列美元价格
    """


    def us_dollar(x):
        yuan = x["价格"]
        return "${:.2f}".format(yuan / 6)


    data["美元价格"] = data.apply(us_dollar, axis=1)
    """
        画图部分
    """
    plt_init()  # 调用画图初始化函数
    plt.xticks(data.index, data["简称"].values, rotation=30)  # 修改x轴显示标签
    plt.plot(data.index, data.loc[:, "价格"], "-s", color="SpringGreen", linewidth=3, label="￥")  # 绘制线条
    for i in range(len(data)):
        plt.text(i, money[i], money[i])  # 使用for循环将内容放入指定位置
    plt.grid(linestyle=":")  # 显示图表格线
    plt.legend()  # 显示标签
    plt.show()
