# By hefei
# @File : dataprocessing.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取CVS文件并保存数据
data = pd.read_csv(r'E:\可删文件\Python\项目1\LA_temperature_2010_hourly.csv')
# 创建一个新的字段month进行排序
data["month"] = data["DATE"].str[:2]


# 进行排序后计算每个月的平均值
# data = data.groupby("month")["HLY-TEMP-NORMAL"].mean()
def pandas_to_numpy(pandas_data):
    # 将pandas读取的cvs数据转换成numpy的数组进行数据处理
    np_data = np.array(pandas_data)
    # 创建一个新的数组用于存放处理后的数据
    month_data = np.empty([12, 4], dtype=float)
    for i in range(12):
        # 进行字符处理，用于数据的条件判断
        str_value = "0{}".format(i + 1)
        if i >= 9:
            str_value = "{}".format(i + 1)
        # 将数组数据处理后重新整合
        month_data[i][0] = i + 1  # 存放编号，代表月份
        # 存放月份平均值并四舍五入到一位小数
        month_data[i][1] = np.around(np.mean(np_data[np.where(np_data[:, 2] == "{}".format(str_value)), 1]), 1)
        month_data[i][2] = np.max(np_data[np.where(np_data[:, 2] == "{}".format(str_value)), 1])  # 存放月份最大值
        month_data[i][3] = np.min(np_data[np.where(np_data[:, 2] == "{}".format(str_value)), 1])  # 存放月份最小值
    return month_data


def plt_init():
    # 修改配置以显示中文
    plt.rcParams['font.sans-serif']=["SimHei"]
    plt.title("某城市一年的温度变化",fontsize=16)
    # 设置图标xy轴标签("显示文字",fontsize设置线条大小)
    plt.xlabel("month(月)", fontsize=15)
    # 设置图标x轴显示的数字
    plt.xticks(ticks=month_data[:, 0])
    plt.ylabel("temperature(摄氏度)", fontsize=15)


if __name__ == '__main__':
    # 创建一个数组对象并把pandas_set_numpy函数中处理好的函数取出
    month_data = pandas_to_numpy(data)
    plt_init()
    # 创建字典用于存放标签
    color_Dictionary = {1: "men:平均值", 2: "max:最大值",3: "min:最小值"}
    color_list = ["Chartreuse", "red", "Cyan"]
    # 绘画线条(x,y,linewidth=设置线条粗细,'设置线条类型'，color="颜色",linestyle='线条样式',marker='线条类型',markersize="设置点大小")
    for i in range(len(color_list)):
        # 绘画month_data参数，分别是平均值，最大值，最小值
        plt.plot(month_data[:, 0], month_data[:, i + 1], '-s',color=color_list[i], linewidth=3, label=color_Dictionary.get(i+1))
        for j in range(12):
            # 将数值显示到对于点上verticalalignment="top"垂直对其位置
            plt.text(month_data[j][0], month_data[j][i + 1], month_data[j][i + 1], fontsize=10,
                     verticalalignment="top")  # 显示对应数值
    # 打印图列标签
    plt.legend()
    # 打印图表
    plt.show()
    print(data)
