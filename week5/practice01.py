# By hefei
#全部成绩为55，66，77，88，99求平均分，大于平均分的数，以及及格率(及格率=及格人数/总人数)
list_num=[55,66,77,88,99]
avg=sum(list_num)/len(list_num)#平均
list_new=[]

x=0;
#遍历列表list_num且记录大于平均分的数及大于60的数
for i in list_num:
    if i>avg:
        list_new.append(i)
    if i>60:
        x+=1;
print("比平均分大的有：{}".format(list_new))
print("平均分{}".format(avg))
print("及格率为：{:.0%}".format(x/len(list_num)))#.0%表示输出为百分数且只保留小数后0位
