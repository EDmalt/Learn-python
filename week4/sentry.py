# By hefei

#利用哨兵机制实现创建角色名字
name="" #定义一下用户名
answer="n" #这个就是定义的哨兵
while answer=="n" or answer=="N":
    name=input("请输入名字：")
    print("头衔：【薯条】","\n名号："+name)
    answer=input("你是否满意自己的名字？Y/N")
print(name,"进入了世界！")