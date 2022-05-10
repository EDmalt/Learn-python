# By hefei
# @File : python-pandas.py
import pandas as pd

data = pd.read_csv(r'E:\可删文件\Python\项目1\LA_temperature_2010_hourly.csv')
print(data.head(10))
print(data["HLY-TEMP-NORMAL"].mean())
print(data.sort_values(by="HLY-TEMP-NORMAL",axis=0,ascending=True,inplace=False))