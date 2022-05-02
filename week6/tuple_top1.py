# By hefei
# 元组也是一种序列。元组使用括弧“（）”来界定；元组中各元素之间用逗号隔开。元组不支持修改或删除其所包含的元素。
# 运行效率比较高
tuple1 = (1, 2, 3)
tuple2 = tuple((1, 2, 3))
print(tuple2)
tuple3 = (100,)
print(tuple3[0])
del tuple3  # 删除整个元组
tuple4 = (value for value in range(10))
print(tuple4)  # 如果使用推导式的话直接打印只会显示内存地址
# 使用遍历的方式来打印使用推导式的元组
for i in tuple4:
    print(i)
