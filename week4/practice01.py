# By hefei
week="星期一\t星期二\t星期三\t星期四\t星期五\t星期六\t星期天"
day_of_week=3#指定一号是星期几
print(week)
print("\t\t"*(day_of_week-1),end="")
for day in range(1,32):
    if (day+day_of_week-1)%7==0 :
        print(day)
    else:
        print(day, end="\t\t")