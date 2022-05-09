# By hefei
# @File : python-pandas.py
import pandas as pd

a=[1,2,3]

print(pd.Series(a))

#pd.to_csv('E:test.csv')
print(pd.date_range("20200102",periods=10,freq="M"))

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)