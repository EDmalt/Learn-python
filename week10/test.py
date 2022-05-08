# By hefei
# @File : test.py
#定义一个类
class Login:
    # 初始化变量
    def __init__(self, id="", name="", password=""):
        self.__id = id
        self.__name = name
        self.__password = password

    def set_id(self,id:str):
        if  15<len(id)<0 and not id.isalpha():
            print("id格式出错")
        else:
            print("格式没问题")

if __name__ == '__main__':
    login=Login()

    print(login.set_id("sdadsd233"))

