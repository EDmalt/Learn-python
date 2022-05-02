# By hefei
year=eval(input("请输入查询年份："))
month=eval(input("请输入查询月份"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("{0}年{1}月有31天".format(year,month))
elif month==2:
    if year%4==0 and year%100!=0 or year%400==0:
        print("{0}年{1}月有29天".format(year,month))
    else:
        print("{0}年{1}月有28天".format(year, month))
else:
    print("{0}年{1}月有30天".format(year, month))
4
4
