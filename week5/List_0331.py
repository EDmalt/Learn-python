# By hefei
# 列表:[]包着，有序可变的数据类型
# 创建列表两种方式：list=[] \ list= list()

list1 = [i for i in range(0, 10, 2)]
list2 = [i for i in range(1, 10, 2)]
# 列表的拼接
print(list1 + list2)

# 列表的切片
# 中括号中第一位为开始数，第二位为结束数，第三位为步长，负数代表倒数第几个数
list3 = [i for i in range(20)]
print(list3[2:10])  # 第二位开始到第9位结束
print(list3[15:])  # 第十五位开始
print(list3[-1])  # 倒数第二个数
print(list3[13:-2])  # 第13位开始到倒数第三位结束

# sum求和
list_num = [x for x in range(101)]
print(sum(list_num))  # 使用sum求和

# 随机化 random
import random  # 导入random包

random.shuffle(list3)
print(list3)
print(max(list1), min(list1))  # 最大最小值
print(sum(list1) / len(list1))  # 平均数

# 列表与列表进行比较
# 优先两两比较，若得出结果则比较结束，否则继续两两比较
list4 = [33, 44, 55, 66]
list5 = [32, 43, 555, 666]
print(list4 > list5)  # 返回bool类型

# 列表的常用方法
list_operate = []
list_operate.append("123")  # append追加，放在列表最后一位
list_operate.append(123)
print("追加列表操作", list_operate)
list_operate.extend(list1)  # 扩展列表：相当于追加了一个列表
print("扩展列表", list_operate)
list_operate = [233, 233, 233, 222, 222, 221, 21]
print("元素个数", list_operate.count(233))  # 元素的计数，查看当前元素有多少个
print("元素下标", list_operate.index(233))  # 返回元素下标，当有多个相同元素时只返回第一个的下标
list_operate.insert(4, 114514)  # 指定位置追加，第一个为下标值，第二个为插入参数
print("指定位置追加", list_operate)
element = list_operate.pop(4)  # 删除pop
print("删除pop", list_operate, element)
list_operate.remove(21)  # 删除remove，输入属性值
print("remove删除", list_operate)

# 排序
list_random = [i for i in range(20)]
random.shuffle(list_random)
print("原列表", list_random)
list_random.sort()
print("使用sort函数排序后", list_random)
