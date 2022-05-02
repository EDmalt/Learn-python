# By hefei
# 列表:[]包着，有序可变的数据类型
#创建列表两种方式：list=[] \ list= list()
list1=list("金木水火土")#直接存list会讲字符串拆开
print(list1)
print(list1[3])#访问列表元素
list2=list(["金木水火土"])#此方法可以将字符串存为一个元素
print(list2)
list3=[i for i in range(10)]#列表内可以存入表达式
print(list3)
list_even=[i for i in range(0,10,2)]#偶数列表
list_odd=[i for i in range(1,10,2)]#奇数列表
print(list_even,"\n",list_odd)
print(5 in list_even,4 not in list_odd)#查询某数是不是在某数组中